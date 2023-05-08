from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

import holidays
from datetime import datetime, date

from .models import JlsTickets
from visitor.models import JlsVisitors
from cart.models import JlsInvoi


class TicketView(LoginRequiredMixin, View):
    template_name = 'ticket.html'

    def calculateAge(self, birthDate):
        today = date.today()
        age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
        return age
    
    def calculateDiscount(self, method, vdate, visitor):
        discount = 0
        age = self.calculateAge(visitor.v_dob)
        us_holidays = holidays.US()
        # no discount on holidays
        if vdate in us_holidays:
            discount = 0
        else:
            # online purchase
            if method == 'OL':
                discount += 0.05
            # membership
            if visitor.v_type == 'M':
                discount += 0.1
            # age
            if age >= 60 or age < 7:
                discount += 0.15
        return discount

    def calculatePrice(self, price, discount):
        return price*(1-discount)
    
    def get(self, request):
        template = loader.get_template(self.template_name)

        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
        myticket = JlsTickets.objects.filter(v_id=visitor.v_id).order_by('tk_vdate')
        ticket_count = JlsTickets.objects.count()
        context = {
            'myticket': myticket,
            'ticket_count': ticket_count,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template(self.template_name)
        # current logged in user
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()

        if 'add_ticket' in request.POST:
            vdate = request.POST.get('visit date')
            # if the user didn't choose a date
            if vdate == "":
                messages.success(request, "Please select a date to visit")
            else:
                tk = JlsTickets.objects.filter(v_id=visitor.v_id, tk_vdate=vdate)
                # if the user already bought a ticket for that day
                if len(tk) != 0:
                    messages.success(request, "You've already bought a ticket!")
                else: 
                    visitor = JlsVisitors.objects.get(user_id=current_user_id)
                    # create a new tickect for this user of the chosen visit date
                    new_tk = JlsTickets()
                    new_tk.v_id = visitor.v_id
                    new_tk.tk_method = 'OL'
                    new_tk.tk_purdate = timezone.now()
                    new_tk.tk_vdate = vdate
                    new_tk.tk_price = 60 # store the original price or price after discount?
                    new_tk.tk_discount = self.calculateDiscount(new_tk.tk_method, vdate, visitor)
                    new_tk.save()
                    messages.success(request, 'Successfully added')

                    # create a new invoice with the ticket, when there's no invoice
                    temp = JlsInvoi.objects.create(
                        invoi_date=date.today(),
                        invoi_amount=self.calculatePrice(new_tk.tk_price, new_tk.tk_discount),
                        invoi_type='Tickets'
                    )
                    temp.save()

                    # use the newly create invoice id to fill in the ticket invoice id
                    new_tk.invoi_id = temp.invoi_id
                    new_tk.save()
            return redirect(reverse('ticket'))
        else:
            all_tks = JlsTickets.objects.filter(v_id=visitor.v_id)
            all_tk = JlsTickets.objects.filter(v_id=visitor.v_id).first()

            group = JlsInvoi.objects.filter(invoi_id=all_tk.invoi_id)
            #
            # objects_to_delete = MyModel.objects.filter(v_id=37)

            for obj in group:
                obj.delete()
            all_tks.delete()
            messages.success(request, 'Successfully deleted all tickets')
        return redirect(reverse('ticket'))
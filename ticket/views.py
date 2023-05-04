from .models import JlsTickets
from visitor.models import JlsVisitors
from django.shortcuts import render
from datetime import datetime, date
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import holidays


class TicketView(LoginRequiredMixin, View):
    template_name = 'ticket.html'

    def calculateAge(self, birthDate):
        today = date.today()
        age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
        return age
    
    def calculateDiscount(self, method, vdate, visitor):
        discount = 0
        age = self.calculateAge(visitor.v_dob)
        print(age)
        us_holidays = holidays.US()
        if vdate in us_holidays:
            discount = 0
        else:
            if method == 'OL':
                discount += 0.05
            if visitor.v_type == 'M':
                discount += 0.1
            if age >= 60 or age < 7:
                discount += 0.15
        return discount

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        current_user_id = self.request.user.id
        vdate = request.POST.get('visit date')
        if vdate == "":
            messages.success(request, "Please select a date to visit")
        else:
            tk = JlsTickets.objects.filter(v_id=current_user_id, tk_vdate=vdate)
            if len(tk) != 0:
                messages.success(request, "You've already bought a ticket!")
            else: 
                visitor = JlsVisitors.objects.get(user_id=current_user_id)

                new_tk = JlsTickets()
                new_tk.v_id = current_user_id
                new_tk.tk_method = 'OL'
                new_tk.tk_purdate = datetime.today()
                new_tk.tk_vdate = vdate
                new_tk.tk_price = 60
                new_tk.tk_discount = self.calculateDiscount(new_tk.tk_method, vdate, visitor)
                new_tk.save()
                messages.success(request, 'Successfully added')
        return render(request, self.template_name)

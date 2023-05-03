from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsTickets
from django.shortcuts import render, redirect, reverse
from datetime import datetime
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required(login_url='home')
# def ticket(request):
#     ticket = JlsTickets.objects.all().values()
#     template = loader.get_template('ticket.html')
#     context = {
#         'ticket': ticket,
#     }
#     if request.method == 'POST':

#         new_tk = JlsTickets()
#         new_tk.tk_id = 1 # should be incremented
#         new_tk.tk_method = 'OL'
#         new_tk.tk_purdate = datetime.today()
#         new_tk.tk_vdate = datetime.today()
#         new_tk.tk_price = 60
#         new_tk.tk_discount = 0
#         new_tk.save()
#         messages.success(request, 'Successfully added')
#     return HttpResponse(template.render(context, request))

class TicketView(LoginRequiredMixin, View):
    template_name = 'ticket.html'
    # success_url = reverse_lazy('memberships')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        current_user_id = self.request.user.id
        # new_tk = JlsTickets.objects.filter(v_id=current_user_id).first()
        new_tk = JlsTickets()
        new_tk.v_id = current_user_id
        new_tk.tk_id = 1 # should be incremented
        new_tk.tk_method = 'OL'
        new_tk.tk_purdate = datetime.today()
        new_tk.tk_vdate = datetime.today()
        new_tk.tk_price = 60
        new_tk.tk_discount = 0
        new_tk.save()
        messages.success(request, 'Successfully added')
        # visitor.refresh_from_db()
        # return redirect(self.success_url)
        return render(request, self.template_name)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsTickets
from django.shortcuts import redirect, reverse
from datetime import datetime
from django.contrib import messages


@login_required(login_url='home')
def ticket(request):
    ticket = JlsTickets.objects.all().values()
    template = loader.get_template('ticket.html')
    context = {
        'ticket': ticket,
    }
    if request.method == 'POST':

        new_tk = JlsTickets()
        new_tk.tk_id = 1 # should be incremented
        new_tk.tk_method = 'OL'
        new_tk.tk_purdate = datetime.today()
        new_tk.tk_vdate = datetime.today()
        new_tk.tk_price = 60
        new_tk.tk_discount = 0
        print(new_tk.tk_id)
        print(new_tk.tk_method)
        print(new_tk.tk_purdate)
        print()
        new_tk.save()
        messages.success(request, 'Successfully added')
    return HttpResponse(template.render(context, request))

# def add(request):
#     if request.method == 'POST':

#         new_tk = JlsTickets()
#         new_tk.tk_method = 'OL'
#         new_tk.tk_purdate = timezone.now
#         new_tk.tk_price = 60
#         new_tk.save()

#         # request.JlsTickets.tk_method.add('OL')
#         # request.JlsTickets.tk_purdate.add(timezone.now)
#         # request.JlsTickets.tk_vdate.add('OL')
#         # request.JlsTickets.tk_price.add(60)
#         messages.success(request, 'Successfully added')
#         return redirect('home/ticket')

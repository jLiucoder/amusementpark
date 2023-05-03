from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsPay
from django.shortcuts import render


@login_required(login_url='home')
def pay(request):
    payment = JlsPay.objects.all().values()
    template = loader.get_template('pay.html')
    context = {
        'payment': payment,
    }
    return HttpResponse(template.render(context, request))
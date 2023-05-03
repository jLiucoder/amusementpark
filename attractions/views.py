from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsAttractions


@login_required(login_url='home')
def attractions(request):
    myAttractions = JlsAttractions.objects.all().values()
    template = loader.get_template('attractions.html')
    context = {
        'myAttractions': myAttractions,
    }
    return HttpResponse(template.render(context, request))

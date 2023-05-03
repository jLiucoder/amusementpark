from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsShows


# @login_required(login_url='home')
# def shows(request):
#     # template = loader.get_template('cart.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'shows.html')
@login_required(login_url='home')
def shows(request):
    myShows = JlsShows.objects.all().values()
    template = loader.get_template('shows.html')
    context = {
        'myShows': myShows,
    }
    return HttpResponse(template.render(context, request))

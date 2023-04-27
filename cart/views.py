from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsInvoi
from django.shortcuts import redirect, reverse


@login_required(login_url='home')
def cart(request):
    mycart = JlsInvoi.objects.all().values()
    template = loader.get_template('show.html')
    context = {
        'mycart': mycart,
    }
    return HttpResponse(template.render(context, request))

def pay(request):
    return redirect(reverse('pay'))


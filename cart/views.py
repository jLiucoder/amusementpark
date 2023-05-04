from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from visitor.models import JlsVisitors
from ticket.models import JlsTickets
from parking.models import JlsParkings
from .models import JlsInvoi
from django.shortcuts import redirect, reverse


@login_required(login_url='home')
def cart(request):
    # getting the logged in current user
    current_user_id = request.user.id
    visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
    # template used
    template = loader.get_template('cart.html')

    # this goes through all parking the user ordered
    myparking = JlsParkings.objects.filter(v_id=visitor.v_id)
    parking_count = JlsParkings.objects.count()

    context = {
        'myparking': myparking,
        'parking_count': parking_count,
    }

    return HttpResponse(template.render(context, request))


def pay(request):
    return redirect(reverse('pay'))

from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from shows.models import JlsVsi, JlsShows
from visitor.models import JlsVisitors, JlsMember
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

    # tickets
    mytickets = JlsTickets.objects.filter(v_id=visitor.v_id)
    ticket_count = JlsTickets.objects.filter(v_id=visitor.v_id).count()
    # not done yet not sure what to do
    ticketfee = JlsTickets.objects.filter(v_id=visitor.v_id)

    # membership
    mem_number = 0
    if len(JlsMember.objects.filter(v_id=visitor.v_id, )) > 0:
        mem_number = JlsMember.objects.get(v_id=visitor.v_id).mem_id
    ifmem = len(JlsMember.objects.filter(v_id=visitor.v_id, ))

    # shows
    myvsi = JlsVsi.objects.filter(v_id=visitor.v_id)
    vsi_count = JlsVsi.objects.filter(v_id=visitor.v_id).count()

    myparking = JlsParkings.objects.filter(v_id=visitor.v_id)
    parking_count = JlsParkings.objects.filter(v_id=visitor.v_id).count()

    context = {
        'mytickets': mytickets,
        'ticket_count': ticket_count,
        'memnumber': mem_number,
        'ifmem': ifmem,
        'myvsi': myvsi,
        'vsi_count': vsi_count,

        'myparking': myparking,
        'parking_count': parking_count,

    }

    return HttpResponse(template.render(context, request))


def pay(request):
    return redirect(reverse('pay'))

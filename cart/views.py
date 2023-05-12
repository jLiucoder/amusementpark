from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from shows.models import JlsVsi, JlsShows
from stores.models import JlsOrder
from visitor.models import JlsVisitors, JlsMember
from ticket.models import JlsTickets
from parking.models import JlsParkings
from .models import JlsInvoi
from django.shortcuts import redirect, reverse, render


@login_required(login_url='home')
def cart(request):
    # getting the logged in current user

    current_user_id = request.user.id
    visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
    # template used
    template = loader.get_template('cart.html')

    # tickets
    mytickets = JlsTickets.objects.filter(v_id=visitor.v_id, tk_purdate=date.today())
    ticket_count = JlsTickets.objects.filter(v_id=visitor.v_id).count()
    # not done yet not sure what to do
    ticket_totalprice = 0
    if len(mytickets) > 0:
        ticket_totalprice = JlsInvoi.objects.filter(invoi_date=date.today(), jlstickets__v=visitor,
                                                  invoi_type='Tickets').first().invoi_amount

    # membership
    mem_number = 0
    mem_price = 0
    ifmem = len(JlsMember.objects.filter(v_id=visitor.v_id))
    if ifmem > 0:
        mem_number = JlsMember.objects.get(v_id=visitor.v_id).mem_id
        mem_price = 99

    # shows
    myvsi = JlsVsi.objects.filter(v_id=visitor.v_id)
    vsi_count = JlsVsi.objects.filter(v_id=visitor.v_id).count()
    show_unitprice = 0
    show_totalprice = 0

    if len(JlsInvoi.objects.filter(invoi_date=date.today(), jlsvsi__v=visitor, invoi_type='Shows')) > 0:
        show_totalprice = JlsInvoi.objects.filter(invoi_date=date.today(), jlsvsi__v=visitor,
                                                  invoi_type='Shows').first().invoi_amount
        show_unitprice = int(show_totalprice/vsi_count)

    # parking
    myparking = JlsParkings.objects.filter(v_id=visitor.v_id)
    parking_count = JlsParkings.objects.filter(v_id=visitor.v_id).count()

    parking_totalprice = 0
    if len(JlsInvoi.objects.filter(invoi_date=date.today(), jlsparkings__v=visitor, invoi_type='Parkings')) > 0:
        store = JlsInvoi.objects.filter(invoi_date=date.today(), jlsparkings__v=visitor, invoi_type='Parkings').first()
        parking_totalprice = store.invoi_amount

    # stores
    mystore = JlsOrder.objects.filter(v_id=visitor.v_id)
    order_count = JlsOrder.objects.filter(v_id=visitor.v_id).count()

    store_totalprice = 0
    if len(JlsInvoi.objects.filter(invoi_date=date.today(), jlsorder__v=visitor, invoi_type='Stores')) > 0:
        store = JlsInvoi.objects.filter(invoi_date=date.today(), jlsorder__v=visitor, invoi_type='Stores').first()
        store_totalprice = store.invoi_amount
    
    total_price = mem_price+ticket_totalprice+show_totalprice+store_totalprice+parking_totalprice

    context = {
        'mytickets': mytickets,
        'ticket_count': ticket_count,
        'ticket_price': ticket_totalprice,

        'memnumber': mem_number,
        'ifmem': ifmem,
        'mem_price': mem_price,

        'myvsi': myvsi,
        'vsi_count': vsi_count,
        'show_unit':show_unitprice,
        'show_price': show_totalprice,

        'myparking': myparking,
        'parking_count': parking_count,
        'parking_price': parking_totalprice,

        'mystore': mystore,
        'order_count': order_count,
        'store_price': store_totalprice,

        'total_price':total_price,
    }

    if request.method == "POST":
        data = request.POST
        print(data)

        if 'delete-membership' in request.POST:
            print('mem')
            visitor.v_type = 'I'
            visitor.save()
            JlsMember.objects.all().delete()
            visitor.refresh_from_db()

            return redirect(reverse('cart'))

        elif 'delete-tickets' in request.POST:
            print('tickets')
            JlsInvoi.objects.filter(jlstickets__v=visitor, invoi_date=date.today(), invoi_type='Tickets').delete()
            # for obj in group:
            #     obj.delete()
            return redirect(reverse('cart'))

        elif 'delete-shows' in request.POST:
            JlsInvoi.objects.filter(jlsvsi__v=visitor, invoi_date=date.today(), invoi_type='Shows').delete()
            # for obj in group:
            #     obj.delete()
            return redirect(reverse('cart'))

        elif 'delete-parkings' in request.POST:
            JlsInvoi.objects.filter(jlsparkings__v=visitor, invoi_date=date.today(), invoi_type='Parkings').delete()
            # for obj in group:
            #     obj.delete()
            return redirect(reverse('cart'))

        elif 'delete-stores' in request.POST:
            JlsInvoi.objects.filter(jlsorder__v=visitor, invoi_date=date.today(), invoi_type='Stores').delete()
            return redirect(reverse('cart'))
        # return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))


# @login_required(login_url='home')
# def post(request):
#     template_name = 'cart.html'
#     current_user_id = request.user.id
#     visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
#     print(visitor.v_id)
#
#
#
#     return render(request, template_name)

@login_required(login_url='home')
def pay(request):
    return redirect(reverse('pay'))

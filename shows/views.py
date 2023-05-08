import decimal
from django.shortcuts import render, redirect
from datetime import date, timezone


from .models import JlsShows, JlsVsi
from cart.models import JlsInvoi
from visitor.models import JlsVisitors


def shows_view(request):
    myShows = JlsShows.objects.all().values()
    if request.method == 'POST':
        show_id = request.POST.get("show_id")
        show_quant = request.POST.get("quantity")

        # get the current user
        current_user_id = request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()

        # get all invoice and filter out the users as today, shows type and current logged in user
        all_invoice = JlsInvoi.objects.all()
        today_pk_usrshow = all_invoice.filter(invoi_date=date.today(), invoi_type='Shows', jlsvsi__v__v_id=visitor.v_id)

        # create temp vsi object
        tempVsi = JlsVsi()
        # if there's already something in the vsi table, we jsut add the quantity to it
        if len(JlsVsi.objects.filter(v_id=visitor.v_id, sh_id=show_id)) > 0:
            tempVsi = JlsVsi.objects.filter(v_id=visitor.v_id, sh_id=show_id).first()
            tempVsi.vsi_quant += int(show_quant)
        # else we populate everything in the vsi table
        else:
            # temp vsi to populate along the way
            tempVsi.v_id = visitor.v_id
            tempVsi.sh = JlsShows.objects.get(sh_id=show_id)
            # get the show quantity here
            tempVsi.vsi_quant = show_quant
            tempVsi.save()

        # calculate the money
        fee = float(tempVsi.sh.sh_price) * float(tempVsi.vsi_quant)

        # if there's something in the invoice table, we jsut add things to it
        if len(today_pk_usrshow) != 0:
            invoi = today_pk_usrshow.first()
            tempVsi.invoi_id = invoi.invoi_id
            invoi.invoi_amount += decimal.Decimal(fee)
            invoi.save()

        else:
            # temp invoice
            tempinvoi = JlsInvoi.objects.create(
                invoi_date=date.today(),
                invoi_amount=fee,
                invoi_type='Shows'
            )
            tempinvoi.save()

            tempVsi.invoi_id = tempinvoi.invoi_id
        tempVsi.save()

        # redirect to success URL
        return redirect('shows')

    # if request.method is GET, render the template with myShows
    return render(request, 'shows.html', {'myShows': myShows})

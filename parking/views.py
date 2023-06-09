from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from cart.models import JlsInvoi
from parking.forms import ParkingForm
from parking.models import JlsParkings
from visitor.models import JlsVisitors


# Create your views here.

class ParkingViewCreate(LoginRequiredMixin, CreateView):
    template_name = 'parking.html'
    form_class = ParkingForm
    success_url = 'parking'

    def form_valid(self, form):
        # Get the current user and their associated visitor
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()

        # Create a new Parking object and set the visitor
        parking = JlsParkings()
        parking.v_id = visitor.v_id
        parking.pk_lot = form.cleaned_data['pk_lot']
        parking.pk_timein = form.cleaned_data['pk_timein']
        parking.pk_timeout = form.cleaned_data['pk_timeout']
        # error checking
        if parking.pk_timeout and parking.pk_timein and parking.pk_timeout < parking.pk_timein:
            raise ValidationError("Invalid input: pk_timeout cannot be less than pk_timein.")

        # calculating the fee here
        duration = (parking.pk_timeout - parking.pk_timein).total_seconds() / 60
        # Calculate the fee based on the duration and the rate
        rate = 18  # dollars per hour
        fee = int(duration / 60 * rate)

        # Print the fee
        parking.pk_fee = fee
        # Save the Parking object to the database
        parking.save()

        # get the current
        all_invoice = JlsInvoi.objects.all()

        today_pk_usrinvoi = all_invoice.filter(invoi_date=date.today(), invoi_type='Parkings', jlsparkings__v__v_id=visitor.v_id)

        if len(today_pk_usrinvoi) != 0:
            invoi = today_pk_usrinvoi.first()
            parking.invoi_id = invoi.invoi_id
            invoi.invoi_amount += parking.pk_fee
            invoi.save()
        else:
            # create a new invoice with the parking fee, when there's no invoice
            temp = JlsInvoi.objects.create(
                invoi_date=date.today(),
                invoi_amount=parking.pk_fee,
                invoi_type='Parkings'
            )
            temp.save()
            parking.invoi_id = temp.invoi_id
        # use the newly create invoice id to fill in the parking invoice id

        parking.save()

        # Redirect to the success URL
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            visitor = JlsVisitors.objects.filter(user_id=self.request.user.id).first()
            count = JlsParkings.objects.filter(v_id=visitor.v_id)
            context["parkingCount"] = len(count)

        return context


class ParkingViewDeleteAll(LoginRequiredMixin, View):
    model = JlsParkings
    success_url = reverse_lazy('parking')
    template_name = 'parkingDelete.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()

        temp = JlsParkings.objects.filter(v_id=visitor.v_id).first()

        # added filter function that deletes from the invoice table,
        # but the logic might not be right since it oonly deletes the invoice for today
        group = JlsInvoi.objects.filter(invoi_id=temp.invoi_id, invoi_date=date.today())
        #
        # objects_to_delete = MyModel.objects.filter(v_id=37)

        for obj in group:
            obj.delete()
        # group.delete()

        return redirect(self.success_url)

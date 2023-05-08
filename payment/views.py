from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from cart.models import JlsInvoi
from visitor.models import JlsVisitors
from .models import JlsPay
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, CreateView
from .forms import PaymentInfoForm


class PayView(LoginRequiredMixin, CreateView):
    template_name = 'pay.html'
    form_class = PaymentInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_Amount'] = self.get_total()
        return context

    def get_total(self):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
        # get current user and the filtered invoice table
        user_total = JlsInvoi.objects.filter(invoi_date=date.today(), jlsvsi__v=visitor, jlstickets__v=visitor,
                                             jlsparkings__v=visitor, jlsorder__v=visitor)
        total = 0

        for i in user_total:
            total += i.invoi_amount
        return total

    def get_success_url(self):
        return reverse('home')

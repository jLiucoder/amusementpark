from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import View

from cart.models import JlsInvoi
from visitor.models import JlsVisitors
from .models import JlsPay
from django.shortcuts import render, redirect
from django.db.models import Q

from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from .forms import PaymentInfoForm


class PaymentView(LoginRequiredMixin, CreateView):
    form_class = PaymentInfoForm
    template_name = 'payment.html'

    def getAmount(self):
        current_user = self.request.user
        visitor = JlsVisitors.objects.filter(v_id=current_user.id).first()

        # complex look up didnt work
        invoicestotal = JlsInvoi.objects.filter(Q(invoi_date=date.today()))

        total_spending = 0

        for i in invoicestotal:
            total_spending += i.invoi_amount

        print(total_spending)

        return total_spending

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context = {
                'total': self.getAmount(),
                'payform': PaymentInfoForm,
            }
        return context

    def get_success_url(self):
        return redirect('paysuccess')

    @transaction.atomic
    # transaction used here
    def form_valid(self, form):

        method = form.cleaned_data['pay_method']
        edate = form.cleaned_data['crd_edate']
        cvv = form.cleaned_data['crd_cvv']
        cnum = form.cleaned_data['crd_num']
        fname = form.cleaned_data['crd_fname']
        lname = form.cleaned_data['crd_lname']

        paydate = date.today()
        # 'pay_method','crd_fname', 'crd_lname', 'crd_num', 'crd_edate', 'crd_cvv'

        tempPay = JlsPay.objects.create(
            pay_method=method,
            pay_date=paydate,
            pay_amount=self.getAmount(),

            crd_fname=fname,
            crd_lname=lname,
            crd_num=cnum,
            crd_cvv=cvv,
            crd_edate=edate

        )
        tempPay.save()
        JlsInvoi.objects.all().delete()
        return redirect('paysuccess')


class PaymentSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'payment_success.html'


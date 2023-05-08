from django import forms
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.forms import fields

from .models import JlsPay, JlsCard

CARDTYPE = [
    ('CREDIT', 'credit'),
    ('DEBIT', 'debit'),
]


class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = JlsPay
        fields = (
            'pay_method', 'pay_date',)
        widgets = {
            'pay_method': forms.Select(choices=CARDTYPE),
            'pay_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class CardInputForm(UserCreationForm):
    class Meta:
        model = JlsCard
        fields = ('crd_fname', 'crd_lname', 'crd_num', 'crd_edate', 'crd_cvv')

        widgets = {
            'crd_edate': forms.widgets.DateInput(attrs={'type': 'date'}),
            'crd_type': forms.Select(choices=CARDTYPE)
        }


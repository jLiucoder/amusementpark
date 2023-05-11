from django import forms
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.forms import fields

from .models import JlsPay

CARDTYPE = [
    ('CREDIT', 'credit'),
    ('DEBIT', 'debit'),
]


class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = JlsPay
        fields = (
            'pay_method','crd_fname', 'crd_lname', 'crd_num', 'crd_edate', 'crd_cvv')
        widgets = {
            'pay_method': forms.Select(choices=CARDTYPE),
            'crd_edate': forms.widgets.DateInput(attrs={'type': 'date'}),
        }





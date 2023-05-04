from django import forms
from django.forms import ModelForm

from .models import JlsTickets


class DateInput(forms.DateInput):
    input_type = 'date'


class TicketForm(ModelForm):

    class Meta:
        model = JlsTickets
        fields = ['tk_id', 'tk_method', 'tk_purdate', 'tk_vdate', 'tk_price', 'tk_discount']
        widgets = {
            'tk_vdate': DateInput(),
        }
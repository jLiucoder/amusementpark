from django import forms
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.forms import fields

from .models import JlsVisitors


class VisitorInfoForm(forms.ModelForm):
    # date = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = JlsVisitors
        fields = (
            'v_fname', 'v_lname', 'v_state', 'v_city', 'v_staddr', 'v_zip', 'v_email', 'v_phone',)
        # 'v_dob', 'v_type',
        widgets = {
            'v_dob': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreateForm,
        'visitorInfo': VisitorInfoForm,
    }

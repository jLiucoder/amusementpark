from django import forms

from parking.models import JlsParkings


SECTION= [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ]

class ParkingForm(forms.ModelForm):
    # date = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = JlsParkings
        fields = (
            'pk_lot', 'pk_timein', 'pk_timeout'
        )
        #  'v_type',
        widgets = {

            'pk_lot': forms.Select(choices=SECTION),
            'pk_timein': forms.widgets.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
            'pk_timeout': forms.widgets.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'})
        }

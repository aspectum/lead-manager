from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class DateTimeForm(forms.Form):
    datetime_field = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
                'format': 'DD/MM/YYYY HH:mm',
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
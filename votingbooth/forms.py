from django import forms
from django.forms import ModelForm
from .models import Election
from bootstrap_datepicker_plus import DatePickerInput

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class ElectionForm(ModelForm):
    class Meta:
        model = Election
        fields = ['Question', 'Start_date', 'End_date']
        widgets = {
            'Start_date':DatePickerInput(format='%d-%m-%y'),
            'End_date':DatePickerInput(format='%d-%m-%y')
        }
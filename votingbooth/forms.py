from django import forms
from django.forms import ModelForm
from .models import Election
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import DateInput


class ElectionForm(ModelForm):
    class Meta:
        model = Election
        fields = ['Question', 'Start_date', 'End_date']
        widgets = {
            'Start_date': DateInput(attrs={'type': 'date'}),
            'End_date': DateInput(attrs={'type': 'date'}),
        }


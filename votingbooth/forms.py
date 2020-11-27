from django import forms
from django.forms import ModelForm
from .models import Election,Answers
from bootstrap_datepicker_plus import DatePickerInput

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
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
            'Start_date':DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True}),
            'End_date':DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True})
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answers   
        fields = ['Answer']     
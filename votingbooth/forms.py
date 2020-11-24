from django import forms 
from .models import Election

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class ElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = ['Question', 'Start_date', 'End_date']
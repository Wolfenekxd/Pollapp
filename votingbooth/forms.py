from django import forms
from django.forms import ModelForm
from .models import Election,Answers
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


            'Start_date':DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True}),
            'End_date':DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True})
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answers   
        fields = ['Answer']     


from django import forms
from django.forms import ModelForm

from .models import allocations


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AllocationForm(ModelForm):

    class Meta:
        model = allocations
        fields = ['police', 'zone', 'date', 'time']
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
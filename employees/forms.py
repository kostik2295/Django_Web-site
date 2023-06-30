from dataclasses import fields
from .models import Employees
from django.forms import ModelForm, Select, TimeInput


class EmpForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

        widgets = {
            'employe' : Select(),
            'work_time' : TimeInput(attrs={
                'placeholder':'Рабочее время'
            }),
            'productivity' : Select(),
        }
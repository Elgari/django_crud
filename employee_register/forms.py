from dataclasses import field
from django import forms
from employee_register.models import crud_employee


class employee_form(forms.ModelForm):
    class Meta:
        model = crud_employee
        fields = '__all__'
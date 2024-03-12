from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname' ,'mobile','employee_id', 'shift')
        labels = {
            'fullname' : 'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__( *args, **kwargs)
        self.fields['shift'].empty_label = "Select"
from django import forms

from .models import application
class ApplicationForm(forms.ModelForm):
    class Meta:

        model = application
        fields=['name', 'gender', 'DOB', 'age', 'phone_number', 'address', 'account_type',]

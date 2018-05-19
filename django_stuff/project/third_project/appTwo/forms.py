from django import forms
from appTwo.models import User
from django.core import validators
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = '__all__'



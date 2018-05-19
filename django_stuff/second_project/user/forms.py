from django.forms import ModelForm
from user.models import User

#Create the form class
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'



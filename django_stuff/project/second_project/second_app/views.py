from django.shortcuts import render
from second_app.models import User
# Create your views here.

def index(request):
    return render(request,'second_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    dict_list = {'users':user_list}
    print(dict_list['users'])
    return render(request,'second_app/users.html',context=dict_list)
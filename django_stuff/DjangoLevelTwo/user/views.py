from django.shortcuts import render
from django.http import HttpResponse
from user.models import User

# Create your views here.
def users(request):
    user_list = User.objects.order_by('first_name')
    dict_list = {'user_dict':user_list}
    print(dict_list['user_dict'])
    return render(request,'user/users.html',context=dict_list)

def index(request):
    return render(request,'user/index.html',context=None)
from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
from user.forms import UserForm

# Create your views here.
#index page
def index(request):
    return render(request,'user/index.html',context=None)

#sign up page
def signup(request):
    if request.method == 'POST':
        #Create a form instance from POST DATA
        f= UserForm(request.POST)
        
        if f.is_valid():
            #Save a new User object from form's data.
            new_user = f.save()
            
            #Create a form to edit an existing User, but use POST data to populate the form
            user = User.objects.get(pk=1)
            form = UserForm(request.POST, instance=user)
            form.save()
            return render(request,'user/index.html')
        else:
            return render(request,'user/index.html')
    else:
        form = UserForm()
        return render(request,'user/signup.html',{'form':form})

#this is for user.html template
def users(request):
    user_list = User.objects.order_by('first_name')
    dict_list = {'user_dict':user_list}
    print(dict_list['user_dict'])
    return render(request,'user/users.html',context=dict_list)


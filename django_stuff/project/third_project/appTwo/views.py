from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import UserForm
def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return render(request,'appTwo/index.html')
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'appTwo/user.html',{'form':form})

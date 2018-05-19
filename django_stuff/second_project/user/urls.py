from django.urls import path
from user import views
urlpatterns = [
    path('',views.index,name="index"),
    path('users/',views.users,name="users"),
    path('signup/',views.signup,name="signup"),
]
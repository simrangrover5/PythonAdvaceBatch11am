from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index),  # localhost --> domain
    path("login/", views.login),
    path("afterlogin/", views.afterlogin),
    path("register/", views.register),
    path("aftersignup/", views.Aftersignup.as_view())
]
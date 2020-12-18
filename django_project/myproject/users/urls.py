from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index),  # localhost --> domain
    path("login/", views.login),
    path("afterlogin/", views.afterlogin),
    path("register/", views.register),
    path("aftersignup/", views.Aftersignup.as_view()),
    path("logout/", views.logout),
    path("forgot/", views.forgot),
    path("sendotp/", views.sendotp),
    path("checkotp/", views.checkotp)
]
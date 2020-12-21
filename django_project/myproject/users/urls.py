from django.urls import path, include
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
    path("checkotp/", views.checkotp),
    path("user/profile/", views.profile),
    path("change/", views.change),
    path("changepass/", views.changepass),
    path("blog/", include("blog.urls"))
]
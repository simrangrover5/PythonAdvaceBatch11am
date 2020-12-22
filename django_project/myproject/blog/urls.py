from django.urls import path, include
from . import views 

urlpatterns = [
    path("addblog/", views.addblog, name="addblog"),
    path("blogadd/", views.Blogadd.as_view()),
    path("myblog/", views.myblog),
    path("api/", views.GetApi.as_view()) # localhost/blog/api
]
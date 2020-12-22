from django.shortcuts import render, redirect
from .forms import Addblog
from django.views import View 
from users.models import Adduser
from .models import Blog
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
# Create your views here.
def addblog(request):
    form = Addblog()
    return render(request, "addblog.html", {"form" : form})

class Blogadd(View):
    def get(self, request):
        return redirect("/blog/addblog/")
    
    def post(self, request):
        form = Addblog(request.POST)
        if form.is_valid():
            data = { 
                "title" : form.cleaned_data['title'],
                "post" : form.cleaned_data['post'],
                "category" : form.cleaned_data['category']
            }
            author = Adduser.objects.get(email=request.session.get("email"))
            data['author'] = author 
            Blog.objects.create(**data) 
            msg = "Blog Added Sucessfully"
            return render(request, "afterlogin.html", {"msg" : msg})
        else:
            msg = "INVALID FORM"
            return redirect("addblog", {"msg" : msg})

def myblog(request):
    obj = Adduser.objects.get(email=request.session.get("email"))
    blogs = Blog.objects.filter(author=obj)
    data = []
    if blogs:
        for obj in blogs:
            d = {
                "title" : obj.title,
                "post" : obj.post,
                "author" : obj.author.username,
                "date" : obj.date
            }
            data.append(d)
        return render(request, "show.html", {"data" : data})
    else:
        msg = "No Blogs Available"
        return render(request, "afterlogin.html", {"msg" : msg})
    
class GetApi(APIView):
    def get(self, request):
        all_blogs = Blog.objects.all()
        blogs = BlogSerializer(all_blogs, many=True)
        return Response(blogs.data)

    def post(self, request):
        print(request.POST)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("This is APP1 App")
    return render(request, "one.html")
    # templates --> one.html
    # templates --> html --> one.html
    # render(request, "html/one.html")


# create project with name my project
# create 2 apps with name users, blog
# return index.html page when request for localhost
# create form in django

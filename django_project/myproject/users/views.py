from django.shortcuts import render, HttpResponse
from .forms import *  # from forms.py import Login Class

# Create your views here.
def index(request):
    return render(request, "nav.html")

def login(request):
    obj = Login()
    return render(request, "login.html", {'form' : obj})

def afterlogin(request):
    form = Login(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        return HttpResponse(f"{email} and {password}")
    else:
        msg = "Invalid Details"
        form = Login()
        return render(request, "login.html", {"form" : form, "msg" : msg})
    
def register(request):
    form = Signup()
    return render(request, "signup.html", {'form' : form})

# users --> urls, project --> urls

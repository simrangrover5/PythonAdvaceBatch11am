from django.shortcuts import render, HttpResponse
from .forms import *  # from forms.py import Login Class
from django.views import View
from .models import Adduser
from random import randint

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

class Aftersignup(View):
    def get(self, request):
        form = Signup()        
        return render(request, "signup.html", {'form' : form})
    
    def post(self, request):
        form = Signup(request.POST)
        if form.is_valid():
            confirm = form.cleaned_data['con_password']
            email = form.cleaned_data['email']
            data = {
                "fname" : form.cleaned_data['fname'],
                "lname" : form.cleaned_data['lname'],
                "email" : form.cleaned_data['email'], # simran.grover@gmail.com, simran.grover@grras.com
                "password" : form.cleaned_data['password'],
            } # for domain make like simran.grover.gmail
            username = email.split("@")[0]
            if Adduser.objects.filter(username=username):
                print("hello")
                possible = []
                for i in range(7):
                    possible.append(username + str(randint(0,999)))
                for i in possible:
                    if not Adduser.objects.filter(username=i):
                        username = i 
            data['username'] = username 
            if confirm == data['password']:
                 Adduser.objects.create(**data)
                 msg = "LOGIN TO CONTINUE..."
                 form = Login()
                 return render(request, "login.html", {'form' : form, 'msg' : msg})
            else:
                msg = "PASSWORD DOES NOT MATCHED...TRY AGAIN"
                form = Signup()
                return render(request, "signup.html", {"form" : form, "msg" : msg})

# users --> urls, project --> urls

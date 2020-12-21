from django.shortcuts import render, HttpResponse, redirect
from .forms import *  # from forms.py import Login Class
from django.views import View
from .models import Adduser
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
    return render(request, "nav.html")

def login(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
    obj = Login()
    return render(request, "login.html", {'form' : obj})

def afterlogin(request):
    if request.method == "GET":
        if request.session.get("islogin"):
            return render(request, "afterlogin.html")
        form = Login()
        return render(request, "login.html", {"form" : form})
    else: 
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                obj = Adduser.objects.get(email=email)
            except Exception as error:
                msg = "No Such User"
                form = Login()
                return render(request, "login.html", {"msg" : msg, "form" : form})
            else:
                if obj.password == password:
                    request.session['email'] = email 
                    request.session['islogin'] = "true"
                    #return HttpResponse(f"{email} and {password}")
                    return render(request, "afterlogin.html")
                else:
                    msg = "Password Is Not Correct"
                    form = Login()
                    return render(request, "login.html", {"msg" : msg, "form" : form})

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
        form = Signup(request.POST, request.FILES)
        if form.is_valid():
            confirm = form.cleaned_data['con_password']
            email = form.cleaned_data['email']
            try:
                Adduser.objects.get(email=email)
            except Exception as error:
                data = {
                    "fname" : form.cleaned_data['fname'],
                    "lname" : form.cleaned_data['lname'],
                    "email" : form.cleaned_data['email'], # simran.grover@gmail.com, simran.grover@grras.com
                    "password" : form.cleaned_data['password'],
                    "image" : form.cleaned_data['image']
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
            else:
                msg = "Email Already Exists...."
                form = Signup()
                return render(request, "signup.html", {"msg" : msg, "form" : form})
        else:
            msg = "Invalid Form...."
            form = Signup()
            return render(request, "signup.html", {"msg" : msg, "form" : form})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    return redirect("/")

def forgot(request):
    form = GetEmail()
    return render(request, "getemail.html", {'form' : form}) 

def sendotp(request):
    form = GetEmail(request.POST)
    if request.method == "GET":
        return redirect("/")
    else:
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                obj = Adduser.objects.get(email=email)
            except Exception as error:
                msg = "Email Does Not Exists"
                form = GetEmail()
                return render(request, "getemail.html", {'form' : form, 'msg' : msg})
            else:
                otp =  randint(1000, 9999)
                subject = "OTP TO CHANGE PASSWORD"
                msg = f"""Welcome to BlogWeb 
                Here is your otp to change your password {otp}"""
                to_email = email
                from_email = "simrangrover5@gmail.com"
                try:
                    send_mail(subject, msg, from_email, [to_email], auth_password=settings.EMAIL_HOST_PASSWORD)
                except Exception as error:
                    print(error)
                    msg = "SERVER IS DOWN....TRY AGAIN"
                    form = Login()
                    return render(request, "login.html", {"form" : form, "msg" : msg})
                else:
                    request.session['otp'] = otp
                    form = Getotp()
                    return render(request, "getotp.html", {"form" : form})
        else:
            msg = "Invalid Form..."
            form = Login()
            return render(request, "login.html", {"form" : form, "msg" : msg})

def checkotp(request):
    if request.method == "GET":
        del request.session['otp']
        return redirect("/")
    else:
        form = Getotp(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            actual = str(request.session.get('otp'))
            if otp == actual:
                return HttpResponse("SUCCESS")
            else:
                del request.session['otp']
                msg = "OTP DOES NOT MATCHED..."
                form = Login()
                return render(request, "login.html", {"msg" : msg, "form" : form})

def profile(request):
    data = Adduser.objects.get(email=request.session.get("email"))
    return render(request, "profile.html", {"data" : data})

def change(request):
    form = Newpass()
    return render(request, "newpass.html", {"form" : form})

def changepass(request):
    if request.method == "GET":
        form = Newpass()
        return render(request, "newpass.html", {"form" : form})
    else: 
        form = Newpass(request.POST)
        if form.is_valid():
            p1 = form.cleaned_data['password']
            p2 = form.cleaned_data['con_password']
            if p1 == p2:
                obj = Adduser.objects.get(email = request.session.get('email'))
                obj.password = p1
                obj.save()
                msg = "Successfully Changed Your Password"
                data = Adduser.objects.get(email=request.session.get("email"))
                return render(request, "profile.html", {"msg" : msg, "data" : data})
            else:
                msg = "Incorrect Password...."
                form = Newpass()
                return render(request, "newpass.html", {"form" : form, "msg" : msg})
# users --> urls, project --> urls
# scenario for making blog website

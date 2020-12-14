from django.http import HttpResponse

def index(request):
    return HttpResponse("THIS IS DJANGO PROJECT")

def home(request):
    return HttpResponse("<h1 style='color:red'>This is My Home With Laptop and Python</h1>")
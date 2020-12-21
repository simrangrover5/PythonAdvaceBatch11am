from django.shortcuts import render
from .forms import Addblog 
# Create your views here.
def addblog(request):
    form = Addblog()
    return render(request, "addblog.html", {"form" : form})


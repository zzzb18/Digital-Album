from django.shortcuts import render
from .models import *
# Create your views here.
def homePage(request):
    topics = Topic.objects.all()
    context = {'topics':topics}
    return render(request,'index.html',context)


def LoginPage(request):
    return render(request,'LoginPage.html')

def RegisterPage(request):
    return render(request,'RegPage.html')
    
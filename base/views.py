from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request,'index.html')

def LoginPage(request):
    return render(request,'LoginPage.html')

def RegisterPage(request):
    return render(request,'RegPage.html')
    
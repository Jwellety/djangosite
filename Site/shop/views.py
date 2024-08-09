from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'shop/home.html')
def aboutus(request):
    return render(request,'shop/aboutus.html')


def signup(request):
    return render(request,'shop/signup.html')
def login(request):
    return render(request,'shop/login.html')
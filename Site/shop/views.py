from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
# Create your views here.

def index(request):
    return render(request,'shop/home.html')

def aboutus(request):
    return render(request,'shop/aboutus.html')

@guest
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'shop/signup.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'shop/login.html',{'form':form}) 

def logout_view(request):
    logout(request)
    return redirect('/')

@auth
def dashboard_view(request):
    return render(request,'shop/dashboard.html')

def community(request):
    return render(request,'shop/community.html')

def event(request):
    return render(request,'shop/event.html')

def faq(request):
    return render(request,'shop/faq.html')

def help(request):
    return render(request,'shop/help.html')

def pricing(request):
    return render(request,'shop/pricing.html')

def privatepolicy(request):
    return render(request,'shop/privatepolicy.html')

def product(request):
    return render(request,'shop/product.html')

def service(request):
    return render(request,'shop/service.html')

def termandcondition(request):
    return render(request,'shop/termandcondition.html')


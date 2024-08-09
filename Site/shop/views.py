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


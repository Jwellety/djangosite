from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .models import UserProfile, ThreeDModel
from .forms import UserProfileForm, ThreeDModelForm

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
    """
    Display and manage user dashboard including profile information
    and 3D model management.
    """
    user = request.user

    # Handle user profile
    user_profile, _ = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST' and 'update_profile' in request.POST:
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    else:
        profile_form = UserProfileForm(instance=user_profile)

    # Handle 3D models
    if request.method == 'POST' and 'add_model' in request.POST:
        model_form = ThreeDModelForm(request.POST, request.FILES)  # Ensure to include request.FILES
        if model_form.is_valid():
            new_model = model_form.save(commit=False)
            new_model.user = user
            new_model.save()
            return redirect('dashboard')
    else:
        model_form = ThreeDModelForm()

    # Fetch all 3D models related to the user
    models = ThreeDModel.objects.filter(user=user)

    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
        'model_form': model_form,
        'models': models,
    }
    return render(request, 'shop/dashboard.html', context)

@auth
def edit_model(request, model_id):
    model = get_object_or_404(ThreeDModel, model_id=model_id, user=request.user)
    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ThreeDModelForm(instance=model)
    return render(request, 'shop/edit_model.html', {'form': form})

@auth
def delete_model(request, model_id):
    """
    Handle the deletion of a 3D model associated with the logged-in user.
    """
    model = get_object_or_404(ThreeDModel, model_id=model_id, user=request.user)
    if request.method == 'POST':
        model.delete()
        return redirect('dashboard')
    return render(request, 'shop/confirm_delete.html', {'model': model})

@auth
def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'shop/update_profile.html', {'form': form})

@auth
def add_model(request):
    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_model = form.save(commit=False)
            new_model.user = request.user
            new_model.save()
            return redirect('dashboard')
    else:
        form = ThreeDModelForm()
    return render(request, 'shop/add_model.html', {'form': form})

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


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('aboutus', views.aboutus, name = 'aboutus'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login')

]
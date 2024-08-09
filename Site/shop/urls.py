from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('aboutus', views.aboutus, name = 'aboutus'),
    path('signup', views.signup, name = 'signup'),
    path('community', views.community, name = 'community'),
    path('event', views.event, name = 'event'),
    path('faq', views.faq, name = 'faq'),
    path('help', views.help, name = 'help'),
    path('login', views.login, name = 'login'),
    path('pricing', views.pricing, name = 'pricing'),
    path('privatepolicy', views.privatepolicy, name = 'privatepolicy'),
    path('product', views.product, name = 'product'),
    path('service', views.service, name = 'service'),
    path('termandcondition', views.termandcondition, name = 'termandcondition'),
]
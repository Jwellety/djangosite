from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('aboutus', views.aboutus, name = 'aboutus'),
    path('signup', views.signup_view, name = 'signup'),
    path('community', views.community, name = 'community'),
    path('event', views.event, name = 'event'),
    path('faq', views.faq, name = 'faq'),
    path('help', views.help, name = 'help'),
    path('logout', views.logout_view, name = 'logout'),
    path('login', views.login_view, name = 'login'),
    path('pricing', views.pricing, name = 'pricing'),
    path('privatepolicy', views.privatepolicy, name = 'privatepolicy'),
    path('product', views.product, name = 'product'),
    path('service', views.service, name = 'service'),
    path('termandcondition', views.termandcondition, name = 'termandcondition'),
    path('dashboard', views.dashboard_view, name = 'dashboard'),
]
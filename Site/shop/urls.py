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
    path('delete_model/<str:model_id>/', views.delete_model, name='delete_model'),
    path('edit_model/<str:model_id>/', views.edit_model, name='edit_model'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('add_model', views.add_model, name='add_model'),

]
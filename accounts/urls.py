from django.urls import path
from . import views

urlpatterns = [
    path('register_vendor', views.register_vendor, name='register_vendor'),
    path('register_customer', views.register_customer, name='register_customer'),
    path('intermediate', views.intermediate, name='intermediate'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

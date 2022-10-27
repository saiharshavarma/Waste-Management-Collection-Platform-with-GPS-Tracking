from django.urls import path
from . import views

urlpatterns = [
    path('register_vendor', views.register_vendor, name='register_vendor'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

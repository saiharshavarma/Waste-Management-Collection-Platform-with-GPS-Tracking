from django.urls import path
from . import views

urlpatterns = [
    path('book_raddiwala', views.book_raddiwala, name='book'),
]

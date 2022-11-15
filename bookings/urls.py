from django.urls import path
from . import views

urlpatterns = [
    path('book_raddiwala', views.book_raddiwala, name='book'),
    path('view_bookings', views.view_bookings, name="bookings"),
    path('confirmed_bookings', views.confirmed_bookings, name="confirmed_bookings"),
    path('accept_deny', views.accept_deny, name="accept_deny"),
    path('accept', views.accept, name="accept"),
    path('collected', views.collected, name="collected"),
]

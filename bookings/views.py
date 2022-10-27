from django.shortcuts import render
from .models import Booking
import pandas
from datetime import datetime
# Create your views here.


def book_raddiwala(request):
    if request.method == "POST":
        user = request.user
        date = datetime.strptime(request.POST['date'], '%Y/%m/%d')
        date = date.strftime('%Y-%m-%d')
        time = datetime.strptime(request.POST['time'], '%H:%M %p')
        time = time.strftime("%H:%M")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        state = str(request.POST['state'])
        zipcode = request.POST['zip']
        email = request.POST['email']
        mobile = request.POST['mobile']
        booking = Booking.objects.create(user=user, date=date, time=time, first_name=first_name, last_name=last_name,
                                         address=address, city=city, state=state, zipcode=zipcode, email=email, mobile=mobile)
        booking.save()
        return render(request, "book-form.html", {})
    else:
        return render(request, "book-form.html", {})

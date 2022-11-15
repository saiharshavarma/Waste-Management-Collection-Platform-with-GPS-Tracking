from django.shortcuts import render, redirect
from .models import Booking, Order
from accounts.models import Profile
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
        return redirect('home')
    else:
        return render(request, "book-form.html", {})


def view_bookings(request):
    booking = Order.objects.get(vendor=Profile.objects.get(user=request.user))
    source = booking.vendor_location
    destination = str(booking.customer.address) + \
        ", " + str(booking.customer.city)
    customer_name = str(booking.customer.first_name) + \
        " " + str(booking.customer.last_name)
    phone_no = str(booking.customer.mobile)
    context = {
        'source': source,
        'destination': destination,
        'customer_name': customer_name,
        'phone_no': phone_no
    }
    return render(request, "view_bookings.html", context)


def confirmed_bookings(request):
    try:
        b = Booking.objects.filter(status=False).order_by('-id')[0]
        booking = Order.objects.get(
            customer=Booking.objects.get(user=request.user))
        if b.status == "False":
            return render(request, "no_bookings.html", {})
        else:
            source = booking.vendor_location
            destination = str(booking.customer.address) + \
                ", " + str(booking.customer.city)
            vendor_name = str(booking.vendor.user.first_name) + \
                " " + str(booking.vendor.user.last_name)
            phone_no = str(booking.vendor.mobile)
            context = {
                'source': source,
                'destination': destination,
                'vendor_name': vendor_name,
                'phone_no': phone_no
            }
            return render(request, "confirmed_booking.html", context)
    except:
        return render(request, "no_bookings.html", {})


def accept_deny(request):
    try:
        booking = Booking.objects.filter(status=False).order_by('-id')[0]
        first_name = booking.first_name
        last_name = booking.last_name
        name = first_name + ' ' + last_name
        address = booking.address
        context = {
            'name': name,
            'address': address
        }
        return render(request, "booking_accept_deny.html", context)
    except:
        return render(request, "no_bookings_currently.html", {})


def accept(request):
    b = Booking.objects.filter(status=False).order_by('-id')[0]
    order = Order.objects.create(
        vendor=Profile.objects.get(user=request.user), customer=b, vendor_location="VIT University, Main Building, VIT University, Vellore, Tamil Nadu, India")
    order.save()
    return redirect('bookings')


def collected(request):
    b = Booking.objects.filter(status=False).order_by('-id')[0]
    b.update()
    return redirect('home')

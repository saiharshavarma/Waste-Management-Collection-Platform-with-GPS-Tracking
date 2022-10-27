from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile, ProfileType
from django.contrib import messages


def register_vendor(request):
    if request.method == 'POST':
        name = request.POST['name']
        first_name, last_name = name.split(' ', 1)
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        profiletype = ProfileType.objects.get(category="Raddiwala")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_vendor')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register_vendor')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print("User saved")
                profile = Profile.objects.create(
                    user=user, mobile=mobile, category=profiletype)
                profile.save()
                print("Profile saved")
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register_vendor')
    else:
        return render(request, 'accounts/signup_vendor.html')


def register_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        first_name, last_name = name.split(' ', 1)
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        profiletype = ProfileType.objects.get(category="Customer")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_customer')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register_customer')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print("User saved")
                profile = Profile.objects.create(
                    user=user, mobile=mobile, category=profiletype)
                profile.save()
                print("Profile saved")
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register_customer')
    else:
        return render(request, 'accounts/signup_customer.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('register_vendor')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/signin.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def intermediate(request):
    return render(request, 'accounts/intermediate.html')


def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def rate(request):
    return render(request, 'rate.html')

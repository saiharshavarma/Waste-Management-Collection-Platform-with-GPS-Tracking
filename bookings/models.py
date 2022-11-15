from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    email = models.EmailField()
    mobile = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.date}' + ' ' + f'{self.mobile}')

    def update(self):
        self.status = True
        super().save()


class Order(models.Model):
    vendor = models.OneToOneField(Profile, on_delete=models.CASCADE)
    customer = models.OneToOneField(Booking, on_delete=models.CASCADE)
    vendor_location = models.CharField(max_length=100)

    def __str__(self):
        return str(f'{self.vendor.user.first_name}' + ' ' + f'{self.customer.user.first_name}' + ' ' + f'{self.vendor_location}')

    def update(self):
        self.status = True
        super().save()

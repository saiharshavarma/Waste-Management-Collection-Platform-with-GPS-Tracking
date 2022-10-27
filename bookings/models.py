from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.date}' + ' ' + f'{self.mobile}')

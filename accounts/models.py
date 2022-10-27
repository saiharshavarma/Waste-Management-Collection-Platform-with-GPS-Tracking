from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileType(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.category)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(unique=True)
    category = models.ForeignKey(
        ProfileType, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.mobile}' + ' ' + f'{self.category}')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.name) + str(self.email)

from django.contrib import admin
from .models import Profile, ProfileType, Contact

# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfileType)
admin.site.register(Contact)

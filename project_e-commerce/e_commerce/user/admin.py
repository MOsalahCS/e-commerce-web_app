from django.contrib import admin

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Useraddress)
admin.site.register(OTPToken)
admin.site.register(CustomUser)


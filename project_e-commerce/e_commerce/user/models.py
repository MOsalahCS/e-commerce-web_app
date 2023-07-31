from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django_countries.fields import CountryField

# Create your models here.
#mhd
User=get_user_model()

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    avatar=models.ImageField()
    bio=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user
    



class Useraddress(models.Model):
    BILLING='B'
    SHIPPING ='S'
    ADDRESS_TYPE=[ BILLING, SHIPPING]
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    country=CountryField()
    street_address=models.CharField(max_length=100)
    apartment_address=models.CharField(max_length=100)
    postal_code=models.CharField( max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.user



    

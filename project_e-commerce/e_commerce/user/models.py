from django_countries.fields import CountryField
from django.db import models
import datetime

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
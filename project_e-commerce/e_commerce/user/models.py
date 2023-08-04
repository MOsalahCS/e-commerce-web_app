from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django_countries.fields import CountryField
import secrets
# Create your models here.
#user model
User=get_user_model()
#user profile with ordering meta
class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    avatar=models.ImageField()
    bio=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_at'] 


    def __str__(self):
        return self.user.get_username()
    


#user address with ordering meta
class Useraddress(models.Model):
    BILLING='B'
    SHIPPING ='S'
    ADDRESS_TYPE=[ BILLING, SHIPPING]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    country=CountryField()
    street_address=models.CharField(max_length=100)
    apartment_address=models.CharField(max_length=100)
    postal_code=models.CharField( max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self) :
        return self.user.get_username()


class OTPToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_token(self):
        # Generate a random 6-digit OTP token
        return secrets.randbelow(1000000)

    def save(self, *args, **kwargs):
        # Generate and save a new OTP token before saving the object
        self.token = self.generate_token()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}: {self.token}"

    

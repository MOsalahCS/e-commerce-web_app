from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin #user model
import datetime
from django_countries.fields import CountryField
import secrets


# Custom User Model

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)




class CustomUser(AbstractUser,PermissionsMixin):

    username=None
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    

    objects=UserManager()
   
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[] 
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    def __str__(self):
        return self.name or self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.email
    




#user profile with ordering meta
class UserProfile(models.Model):
    user=models.OneToOneField(CustomUser,related_name='profile', on_delete=models.CASCADE)
    avatar=models.ImageField()
    bio=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_at'] 


    def __str__(self):
        return self.user.get_full_name()
    


#user address with ordering meta
class Useraddress(models.Model):
    BILLING='B'
    SHIPPING ='S'
    ADDRESS_TYPE=[ BILLING, SHIPPING]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
        return self.city


class OTPToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_token(self):
        
        return secrets.randbelow(1000000)

    def save(self, *args, **kwargs):
       
        self.token = self.generate_token()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.name}: {self.token}"

    


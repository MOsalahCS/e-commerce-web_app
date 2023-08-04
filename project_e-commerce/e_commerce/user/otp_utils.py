from django.core.mail import send_mail
import pyotp
from .models import * 
import base64
import secrets
from django.http import HttpResponseBadRequest 
from rest_framework.response import Response

def generate_key():
    # Generate a random 20-byte key and encode it in base32
    random_bytes = secrets.token_bytes(20)
    base32_key = base64.b32encode(random_bytes).decode()
    return base32_key

def send_otp_email(user):
    otp_token = pyotp.TOTP(generate_key(), interval=300)  # Generate 6-digit OTP valid for 5 minutes
    otp = otp_token.now()
    OTPToken.objects.create(user=user, token=otp)

    subject = 'Your OTP for Authentication'
    message = f'Your OTP is: {otp}'
    from_email = 'your_email@example.com'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
    
def verify_otp(user, otp):
    otp_token = OTPToken.objects.filter(user=user).order_by('-created_at').first()
    try:

        if otp_token and otp_token.token == otp:
        # OTP is valid, perform your desired action here (e.g., log in the user)
            return True
    except:
            return HttpResponseBadRequest

from django.dispatch import Signal, receiver
# from django.contrib.auth.signals import user_logged_in
# from .models import OTPToken,CustomUser

# user_login_verified = Signal()

# @receiver(user_logged_in)
# def Verify_User_Login(sender, request, user, **kwargs):
#     try:
#         custom_user = CustomUser.objects.get(pk=user.pk)
#         otp_token = OTPToken.objects.get(user=custom_user)
#         user_otp = request.POST.get('otp')
#         verification_status = otp_token.token == user_otp

#         user_login_verified.send(sender=None, user=custom_user, verification_status=verification_status)
#     except OTPToken.DoesNotExist:
#         user_login_verified.send(sender=None, user=custom_user, verification_status=False)

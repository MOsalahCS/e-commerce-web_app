import jwt, datetime
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from .models import CustomUser
def create_access_token(id):
    return jwt.encode(
         {         
        'user_id': id,
    
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        'iat': datetime.datetime.utcnow()
    
},      'access_secret', algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')

        return payload['user_id']
    except:
            raise exceptions.AuthenticationFailed('unauthenticated')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
    

# def decode_jwtandgetheader(request):
       
#         auth=get_authorization_header(request).split()
#         if auth and len(auth)== 2:
#             token=auth[1].decode('utf-8')
             
#             payload = jwt_decode_handler(token)
#             user_id = payload['user_id']
#             decode_access_token(token)
#             user = CustomUser.objects.get(id=user_id)  # Replace with your user model

#             if user.is_superuser:
#                permissions = ['view', 'add', 'change', 'delete']
#             else:
#              permissions = ['view']

#              return permissions
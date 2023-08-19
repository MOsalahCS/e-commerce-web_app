# # permissions.py or your views module
# from rest_framework.permissions import BasePermission
# from .authentication import decode_jwtandgetheader

# class CustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         permissions = decode_jwtandgetheader(request)
#         if permissions is None:
#             return False  # Token is invalid or expired
        
#         required_permission = view.required_permission
#         return required_permission in permissions

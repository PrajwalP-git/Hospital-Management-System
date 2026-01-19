from rest_framework.permissions import BasePermission

class IsStaffOrDoctor(BasePermission):
    def has_permission(self,request,view):
        return request.user and request.user.is_authenticated
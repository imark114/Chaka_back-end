from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'super_admin'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'super_admin']

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['user', 'admin', 'super_admin']

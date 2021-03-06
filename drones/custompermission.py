from rest_framework import permissions

class IsCurrentUserOwnerReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return true;
        else:
            return obj.owner == request.user
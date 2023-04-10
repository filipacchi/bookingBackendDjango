from rest_framework import permissions
from django.contrib.auth.models import Group;
from washbooking.models import *;

class checkGroup(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if Group.objects.get(name='User').user_set.filter(id=request.user.id).exists():
            return True
        return False
      
        
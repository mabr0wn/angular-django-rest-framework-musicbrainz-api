"""
We would like all code exeriments to be visible to anyone, but also make sure
that only the user that created a code experiment is able to update or delete it.

To do that we are going to need to create a custom permission
"""
# Django rest
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  ''' Custom permission to only allow owners of an object to edit it.'''
  
  def has_object_permission(Self, request, view, obj):
      """
      Read permssions are allowed to any request,
      so we will always allow GET, HEAD, or OPTION requests.
      """
      if request.method in permissions.SAFE_METHODS:
          return True
      
      
      ''' Write permissions are only allowed to the owner of the experiment'''
      return obj.owner == request.user

class CustomerAccessPermission(permissions.BasePermission):
    """
    Adding a customer access permission,
    Going to write this soon.
    """
    pass
  
class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs
    """
    
    def has_permission(self,request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted
      
class IsSpecialUserNotAdmin(permissions.BasePermission):
    """
    Customer permission to allow special users to change an object,
    Not quite an admin.
    """
    def special_user_object_permission(self, request, view, obj):
        pass

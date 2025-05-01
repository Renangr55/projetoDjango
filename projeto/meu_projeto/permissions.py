from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework import response
from rest_framework.decorators import APIView

class isGestor(BasePermission):
    def has_object_permission(self, request, view, obj):
            return request.user.is_authenticated and request.user.usuario == 'gest'

class isProfessor(BasePermission):
    def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.usuario == 'prof'
        
    def has_object_permission(self, request, view, obj):
          return obj.professor == request.user
    

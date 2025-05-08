from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS
from .models import Ambiente, Disciplina
from rest_framework.permissions import IsAdminUser
from rest_framework import response
from rest_framework.decorators import APIView


#Permissoões individuais
class IsGestor(BasePermission):
        def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.usuario == 'gest'

class IsProfessor(BasePermission):
        def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.usuario == 'prof'
        
#Permissão para professor ou gestor
class IsProfessorOuGestor(BasePermission):
        def has_permission(self, request, view):
                if request.method in SAFE_METHODS:
                       return request.user.usuario in ['gest','prof'] # professor e gestor tem acesso para listar
                return request.user.usuario == 'gest'
        
        def has_object_permission(self, request, view, obj):
                if request.method in SAFE_METHODS:
                        if request.user.usuario == 'gest': # se o usuario for gestor ele vai ter acesso
                                return True
                        return request.user == obj.professor_responsavel.user #se o user que esta logado for igual o user do professor_responsavel ele vai retornar
                return request.user.usuario == 'gest' #o gestor pode realizar o crud completo
                       



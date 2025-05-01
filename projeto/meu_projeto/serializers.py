from rest_framework import serializers
from .models import Professor, Ambiente, Disciplina, Usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(TokenObtainPairSerializer):
    
    token_class = RefreshToken
    
    def validate(self, attrs):
        dados = super().validate(attrs)
        
        
        dados['usuario'] = {
            'nome' : self.user.username,
            'biografia' : self.user.biografia,
            'escolha' : self.user.usuario,
        }
        
        return dados
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'
        
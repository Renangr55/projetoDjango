from django.urls import path
from .views import(ProfessorListCreateAPIView,
                   ProfessorRetrieveUpdateDestroyAPIView,
                   DisciplinaListCreateAPIView,
                   DisciplinaRetrieveUpdateDestroyAPIView,
                   AmbienteListCreateAPIView,
                   AmbienteRetrieveUpdateDestroyAPIView,
                   UsuarioListCreateAPIView
                   )
from rest_framework_simplejwt.views import(TokenObtainPairView,
                                           TokenRefreshView
                                            )

urlpatterns = [
    #Operação com Professores
    path('Professores',ProfessorListCreateAPIView.as_view()),
    path('Professores/<int:pk>',ProfessorRetrieveUpdateDestroyAPIView.as_view()),
    
    #Operação com Disciplinas
    path('Disciplinas/',DisciplinaListCreateAPIView.as_view()),
    path('Disciplinas/<int:pk>', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),
    
    #Operação com Ambientes
    path('Ambiente', AmbienteListCreateAPIView.as_view()),
    path('Ambiente/<int:pk>', AmbienteRetrieveUpdateDestroyAPIView.as_view()),
    
    #Autenticação
    path('autenticacao/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('autenticacao/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    
    #Criação de usuario
    path('usuario', UsuarioListCreateAPIView.as_view(), name="Usuario")
]
from django.urls import path
from .views import(ProfessorListCreateAPIView,
                   ProfessorRetrieveUpdateDestroyAPIView,
                   DisciplinaListCreateAPIView,
                   DisciplinaRetrieveUpdateDestroyAPIView,
                   AmbienteListCreateAPIView,
                   AmbienteRetrieveUpdateDestroyAPIView
                   )

urlpatterns = [
    path('Professores',ProfessorListCreateAPIView.as_view()),
    path('Professores/<int:pk>',ProfessorRetrieveUpdateDestroyAPIView.as_view()),
    path('Disciplinas/',DisciplinaListCreateAPIView.as_view()),
    path('Disciplinas/<int:pk>', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),
    path('Ambiente', AmbienteListCreateAPIView.as_view()),
    path('Ambiente/<int:pk>', AmbienteRetrieveUpdateDestroyAPIView.as_view())
]
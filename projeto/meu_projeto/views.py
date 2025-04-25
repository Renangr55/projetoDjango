from django.shortcuts import render
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Usuario, Professor, Ambiente, Disciplina
from .serializers import UsuarioSerializer,ProfessorSerializer,AmbienteSerializer,DisciplinaSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

#classe da exibição da quantidade de usuarios
class UsuarioPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


#classe da exibição da quantidade de professor
class ProfessorPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10

#classe da exibição da quantidade de ambientes
class AmbientePagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page-size'
    max_page_size = 10

#classe da exibição da quantidade de ambientes
class DisciplinaPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page-size'
    max_page_size = 10



class ProfessorListCreateAPIView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    pagination_class = ProfessorPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        ni = self.request.query_params.get('ni')
        if ni:
            queryset = queryset.filter(nome__icontains=ni)
        return queryset
    
class ProfessorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Mensagem" : f" deletado com sucesso"}, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"Mensagem" : f" Professor Listado "}, serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False) # tente apagar o paramentro de passado em kwags,mais se não achar retorne False
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        "Se tiver cache de prefetch aqui, limpa! Porque os dados mudaram, e quero que a próxima leitura venha atualizada direto do banco."
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response({'Mensagem': "Dados atualizados com sucesso"}, serializer.data ,status=status.HTTP_200_OK)

class DisciplinaListListCreateAPIView(ListCreateAPIView):
    queryset = Ambiente.objects.all()
    pagination_class = AmbientePagination
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_disciplina = self.request.query_params.get('nome_disciplina')
        if nome_disciplina:
            queryset = queryset.filter(nome__icontains=nome_disciplina)
        return queryset

class DisciplinaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    pagination_class = DisciplinaPagination
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]





    

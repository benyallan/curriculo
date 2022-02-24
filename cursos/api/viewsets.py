from cursos.models import Curso
from .serializers import CursoSerializer
from rest_framework import viewsets


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
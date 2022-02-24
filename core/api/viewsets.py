from core.models import DadosPessoais
from .serializers import DadosPessoaisSerializer
from rest_framework import viewsets


class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer
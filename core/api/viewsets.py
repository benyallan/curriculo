from core.models import DadosPessoais, Telefone
from .serializers import DadosPessoaisSerializer, TelefoneSerializer
from rest_framework import viewsets


class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer


class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
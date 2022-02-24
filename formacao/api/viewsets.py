from .serializers import FormacaoSerializer
from rest_framework import viewsets
from formacao.models import Formacao

class FormacaoViewSet(viewsets.ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
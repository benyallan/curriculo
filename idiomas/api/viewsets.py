from idiomas.models import Idioma
from .serializers import IdiomaSerializer
from rest_framework import viewsets


class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
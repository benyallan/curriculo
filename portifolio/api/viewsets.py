from portifolio.models import Portifolio
from .serializers import PortifolioSerializer
from rest_framework import viewsets


class PortifolioViewSet(viewsets.ModelViewSet):
    queryset = Portifolio.objects.all()
    serializer_class = PortifolioSerializer
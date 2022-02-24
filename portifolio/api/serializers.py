from portifolio.models import Portifolio
from rest_framework.serializers import ModelSerializer


class PortifolioSerializer(ModelSerializer):
    class Meta:
        model = Portifolio
        fields = "__all__"
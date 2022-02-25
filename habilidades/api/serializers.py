from habilidades.models import Habilidade
from rest_framework.serializers import ModelSerializer


class HabilidadeSerializer(ModelSerializer):
    class Meta:
        model = Habilidade
        fields = "__all__"
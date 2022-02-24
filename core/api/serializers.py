from core.models import DadosPessoais
from rest_framework.serializers import ModelSerializer


class DadosPessoaisSerializer(ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = "__all__"
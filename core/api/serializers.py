from core.models import DadosPessoais, Telefone
from rest_framework.serializers import ModelSerializer


class DadosPessoaisSerializer(ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = "__all__"


class TelefoneSerializer(ModelSerializer):
    class Meta:
        model = Telefone
        fields = "__all__"
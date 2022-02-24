from core.models import DadosPessoais
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class DadosPessoaisSerializer(ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = "__all__"
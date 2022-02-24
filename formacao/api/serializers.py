from formacao.models import Formacao
from rest_framework.serializers import ModelSerializer


class FormacaoSerializer(ModelSerializer):
    class Meta:
        model = Formacao
        fields = "__all__"
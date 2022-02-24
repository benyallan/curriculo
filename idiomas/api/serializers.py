from idiomas.models import Idioma
from rest_framework.serializers import ModelSerializer


class IdiomaSerializer(ModelSerializer):
    class Meta:
        model = Idioma
        fields = "__all__"
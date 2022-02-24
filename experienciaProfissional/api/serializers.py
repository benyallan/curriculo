from experienciaProfissional.models import ExperienciaProfissional
from rest_framework.serializers import ModelSerializer


class ExperienciaProfissionalSerializer(ModelSerializer):
    class Meta:
        model = ExperienciaProfissional
        fields = "__all__"
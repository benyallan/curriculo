from django.db import models
from django.core.validators import MaxValueValidator


class Habilidade(models.Model):

    name = models.CharField(("nome"), max_length=150)
    level = models.PositiveSmallIntegerField(
            ("nível"), validators=[MaxValueValidator(10)]
        )
    person = models.ForeignKey(
            "core.dadospessoais", verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("habilidade")
        verbose_name_plural = ("habilidades")

    def __str__(self):
        return self.name

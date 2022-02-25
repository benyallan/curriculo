from django.db import models
from django.core.validators import MaxValueValidator


class Idioma(models.Model):

    name = models.CharField(("nome"), max_length=80)
    level = models.PositiveSmallIntegerField(
            ("nível"), validators=[MaxValueValidator(10)]
        )
    person = models.ForeignKey(
            "core.dadospessoais", verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("idioma")
        verbose_name_plural = ("idiomas")

    def __str__(self):
        return self.name

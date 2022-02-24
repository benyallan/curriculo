from django.db import models
from core.models import DadosPessoais

class ExperienciaProfissional(models.Model):

    enterprise = models.CharField(("empresa"), max_length=200)
    current = models.BooleanField(("atual"), default=False)
    startDate = models.DateField(
            ("data de início"), auto_now=False, auto_now_add=False,
            null=True, blank=True
        )
    endDate = models.DateField(
            ("data de término"), auto_now=False, auto_now_add=False,
            null=True, blank=True
        )
    role = models.CharField(("cargo"), max_length=150)
    description = models.TextField(("descrição das atribuições"))
    city = models.CharField(("município"), max_length=150)
    country = models.CharField(("país"), max_length=150)
    person = models.ForeignKey(
            DadosPessoais, verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("Experiência Profissional")
        verbose_name_plural = ("Experiências Profissionais")

    def __str__(self):
        return self.enterprise

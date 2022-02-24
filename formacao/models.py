from django.db import models


class Formacao(models.Model):

    name = models.CharField(("nome"), max_length=150)
    yearCompletion = models.CharField(("ano de conclusão"), max_length=4)
    institute = models.CharField(("instituição"), max_length=150)
    person = models.ForeignKey(
            "core.dadospessoais", verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("formação")
        verbose_name_plural = ("formações")

    def __str__(self):
        return self.name

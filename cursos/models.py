from django.db import models


class Curso(models.Model):

    name = models.CharField(("nome"), max_length=150)
    school = models.CharField(("instituição de ensino"), max_length=150)
    person = models.ForeignKey(
            "core.dadospessoais", verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("curso")
        verbose_name_plural = ("cursos")

    def __str__(self):
        return self.name

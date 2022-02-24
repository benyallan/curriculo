from django.db import models


class DadosPessoais(models.Model):

    name = models.CharField(("nome"), max_length=250)
    birth = models.DateField(("data de nascimento"), auto_now=False, auto_now_add=False)
    sex = models.CharField(("sexo"), max_length=1)
    adress = models.CharField(("endereço"), max_length=250)
    mail = models.CharField(("e-mail"), max_length=255)
    sumary = models.TextField(("sobre"))
    photo = models.ImageField(("foto"), upload_to=None, height_field=None, width_field=None, max_length=None)
    personalSite = models.URLField(("site pessoal"), max_length=200)

    class Meta:
        verbose_name = ("Dados Pessoais")
        verbose_name_plural = ("Dados Pessoais")

    def __str__(self):
        return self.name

class Telefone(models.Model):

    number = models.CharField(("número"), max_length=15)
    whatsapp = models.BooleanField(("WhatsApp"), default=False)
    telegram = models.BooleanField(("Telegram"), default=False)
    person = models.ForeignKey(
            DadosPessoais, verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("Telefone")
        verbose_name_plural = ("Telefones")

    def __str__(self):
        return self.number

class RedesSociais(models.Model):

    name = models.CharField(("nome"), max_length=150)
    link = models.URLField(("link"), max_length=200)
    person = models.ForeignKey(
            DadosPessoais, verbose_name=("pessoa"), on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = ("Redes Sociais")
        verbose_name_plural = ("Redes Sociais")

    def __str__(self):
        return self.name

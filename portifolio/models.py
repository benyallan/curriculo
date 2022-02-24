from django.db import models

class Portifolio(models.Model):
    link = models.URLField(("link"), max_length=200)
    description = models.TextField(("descrição"))
    
    class Meta:
        verbose_name = 'portifolio'
        verbose_name_plural = 'portifolio'

    def __str__(self):
        return self.link


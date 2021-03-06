# Generated by Django 4.0.2 on 2022-02-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_redessociais_person_telefone_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='adress',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='mail',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='personalSite',
            field=models.URLField(blank=True, null=True, verbose_name='site pessoal'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='sex',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='sexo'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='sumary',
            field=models.TextField(blank=True, null=True, verbose_name='sobre'),
        ),
    ]

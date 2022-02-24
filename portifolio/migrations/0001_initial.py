# Generated by Django 4.0.2 on 2022-02-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='link')),
                ('description', models.TextField(verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'portifolio',
                'verbose_name_plural': 'portifolio',
            },
        ),
    ]
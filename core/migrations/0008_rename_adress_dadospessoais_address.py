# Generated by Django 4.0.2 on 2022-03-01 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_telefone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dadospessoais',
            old_name='adress',
            new_name='address',
        ),
    ]

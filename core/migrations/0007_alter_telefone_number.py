# Generated by Django 4.0.2 on 2022-02-25 18:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_telefone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefone',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
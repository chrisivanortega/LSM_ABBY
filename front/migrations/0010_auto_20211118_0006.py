# Generated by Django 3.2.9 on 2021-11-18 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_auto_20211118_0001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pregunta',
        ),
        migrations.DeleteModel(
            name='Senna',
        ),
    ]
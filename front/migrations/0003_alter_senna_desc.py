# Generated by Django 3.2.9 on 2021-11-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_senna_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senna',
            name='desc',
            field=models.TextField(verbose_name=''),
        ),
    ]

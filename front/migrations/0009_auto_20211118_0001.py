# Generated by Django 3.2.9 on 2021-11-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_alter_senna_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senna',
            name='id',
        ),
        migrations.AlterField(
            model_name='senna',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='senna',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]

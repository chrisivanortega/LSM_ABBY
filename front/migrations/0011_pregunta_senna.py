# Generated by Django 3.2.9 on 2021-11-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('front', '0010_auto_20211118_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Senna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('desc', models.CharField(default='', max_length=200)),
            ],
        ),
    ]

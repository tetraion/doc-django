# Generated by Django 3.2.10 on 2021-12-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(max_length=255, unique=True)),
                ('price', models.CharField(max_length=255, unique=True)),
                ('url', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-08-03 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 8, 3, 13, 39, 45, 552845))),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
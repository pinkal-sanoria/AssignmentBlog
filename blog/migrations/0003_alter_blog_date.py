# Generated by Django 3.2.12 on 2024-04-21 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240421_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 21, 11, 31, 20, 285039)),
        ),
    ]

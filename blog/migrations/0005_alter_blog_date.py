# Generated by Django 3.2.12 on 2024-04-21 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 21, 11, 32, 33, 38032)),
        ),
    ]

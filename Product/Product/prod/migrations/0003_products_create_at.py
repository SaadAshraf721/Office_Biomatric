# Generated by Django 3.0 on 2021-04-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

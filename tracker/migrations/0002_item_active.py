# Generated by Django 3.1.4 on 2021-01-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

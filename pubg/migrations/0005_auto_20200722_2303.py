# Generated by Django 3.0.5 on 2020-07-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0004_auto_20200722_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

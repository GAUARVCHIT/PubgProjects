# Generated by Django 3.0.5 on 2020-07-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0002_auto_20200722_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-07-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0003_auto_20200722_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

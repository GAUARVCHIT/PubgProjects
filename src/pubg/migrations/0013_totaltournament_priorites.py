# Generated by Django 3.0.5 on 2020-10-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0012_playerresult_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='totaltournament',
            name='priorites',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=4, null=True),
        ),
    ]
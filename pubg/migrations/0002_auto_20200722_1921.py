# Generated by Django 3.0.5 on 2020-07-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'verbose_name_plural': 'Sponsor'},
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('short_name', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='teams_logo')),
                ('website_link', models.URLField(blank=True, null=True)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('yt_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('organizations', models.ManyToManyField(blank=True, related_name='organizations_backing_teams', to='pubg.Organizations')),
                ('sponsor', models.ManyToManyField(blank=True, to='pubg.Sponsor')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
    ]

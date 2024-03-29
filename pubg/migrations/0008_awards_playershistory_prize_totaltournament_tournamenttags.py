# Generated by Django 3.0.5 on 2020-07-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0007_peoples'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'TournamentTags',
            },
        ),
        migrations.CreateModel(
            name='TotalTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('short_name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('starting_date', models.DateField(blank=True, null=True)),
                ('endings_date', models.DateField(blank=True, null=True)),
                ('prize_pool', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.Seasons')),
                ('subtournament', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.TotalTournament')),
                ('tags', models.ManyToManyField(blank=True, to='pubg.TournamentTags')),
                ('teams', models.ManyToManyField(related_name='teams_participating_in_tournaments', to='pubg.Teams')),
            ],
            options={
                'verbose_name_plural': 'TotalTournament',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(null=True)),
                ('money', models.PositiveIntegerField(null=True)),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pubg.TotalTournament')),
            ],
            options={
                'verbose_name_plural': 'Prize',
            },
        ),
        migrations.CreateModel(
            name='PlayersHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active Squad', 'Active Squad'), ('Former Players', 'Former Players'), ('Temporary stand-ins', 'Temporary stand-ins')], max_length=50, null=True)),
                ('people', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.Peoples')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.Teams')),
            ],
            options={
                'verbose_name_plural': 'TournamentTags',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('award_money', models.PositiveIntegerField(null=True)),
                ('side_benfits', models.TextField(blank=True, null=True)),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pubg.TotalTournament')),
            ],
            options={
                'verbose_name_plural': 'Awards',
            },
        ),
    ]

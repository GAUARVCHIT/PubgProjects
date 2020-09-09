# Generated by Django 3.0.5 on 2020-07-23 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0010_auto_20200723_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Maps',
            },
        ),
        migrations.CreateModel(
            name='PointsTableType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'PointsTableType',
            },
        ),
        migrations.CreateModel(
            name='TournamentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, null=True)),
                ('teams_in_group', models.ManyToManyField(to='pubg.Teams')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.TotalTournament')),
            ],
            options={
                'verbose_name_plural': 'TournamentGroup',
            },
        ),
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField(null=True)),
                ('placement_point', models.PositiveIntegerField(null=True)),
                ('kill_points', models.PositiveIntegerField(default=1, null=True)),
                ('pointsTableType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.PointsTableType')),
            ],
            options={
                'verbose_name_plural': 'PointsTable',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(blank=True, choices=[('Day 1', 'Day 1'), ('Day 2', 'Day 2'), ('Day 3', 'Day 3'), ('Day 4', 'Day 4'), ('Day 5', 'Day 5')], max_length=20, null=True)),
                ('match_starting_time', models.DateTimeField(blank=True, null=True)),
                ('tournament_match_no', models.CharField(blank=True, choices=[('Match 1', 'Match 1'), ('Match 2', 'Match 2'), ('Match 3', 'Match 3'), ('Match 4', 'Match 4'), ('Match 5', 'Match 5'), ('Match 6', 'Match 6')], max_length=10, null=True)),
                ('maps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.Maps')),
                ('teams', models.ManyToManyField(to='pubg.Teams')),
                ('total_tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubg.TotalTournament')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]

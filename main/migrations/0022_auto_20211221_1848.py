# Generated by Django 3.2.9 on 2021-12-21 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_fantasyteam_matchup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchup',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team1', to='main.fantasyteam'),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team2', to='main.fantasyteam'),
        ),
    ]
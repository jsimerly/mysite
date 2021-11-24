# Generated by Django 3.2.9 on 2021-11-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211124_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerhistory',
            name='season',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playerhistory',
            name='week',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teamhistory',
            name='ml',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='teamhistory',
            name='ou',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='teamhistory',
            name='score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='teamhistory',
            name='season',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teamhistory',
            name='week',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sleeperId',
            field=models.CharField(max_length=6, null=True),
        ),
    ]

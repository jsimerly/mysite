# Generated by Django 3.2.9 on 2021-11-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211124_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='fantasyteam',
            name='rosterId',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_serverinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverinfo',
            name='lastProjUpdate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='lastLineUpdate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='lastMatchupUpdate',
            field=models.DateTimeField(null=True),
        ),
    ]

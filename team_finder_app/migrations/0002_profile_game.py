# Generated by Django 5.0.2 on 2024-05-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_finder_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='game',
            field=models.CharField(default='Dota 2', max_length=20),
        ),
    ]

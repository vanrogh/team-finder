# Generated by Django 5.0.2 on 2024-05-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_finder_app', '0003_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='game',
            field=models.CharField(choices=[('Dota 2', 'Dota 2'), ('CS:2', 'CS:2'), ('CoD Warzone', 'CoD Warzone'), ('LoL', 'LoL'), ('Apex Legends', 'Apex Legends'), ('Valorant', 'Valorant'), ('Fortnite', 'Fortnite')], max_length=20),
        ),
    ]

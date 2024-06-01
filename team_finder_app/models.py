from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    discord = models.CharField(max_length=100)
    steam = models.CharField(max_length=100)
    epic_games = models.CharField(max_length=100, blank=True, null=True)
    ubisoft = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    game_choices = [
        ('Dota 2', 'Dota 2'),
        ('CS:2', 'CS:2'),
        ('CoD Warzone', 'CoD Warzone'),
        ('LoL', 'LoL'),
        ('Apex Legends', 'Apex Legends'),
        ('Valorant', 'Valorant'),
        ('Fortnite', 'Fortnite'),
    ]
    game = models.CharField(max_length=20, choices=game_choices)


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
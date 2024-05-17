from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    game_choices = [
        ('Dota 2', 'Dota 2'),
        ('CS:2', 'CS:2'),
        ('CoD Warzone', 'CoD Warzone'),
        ('LoL', 'LoL'),
        ('Apex Legends', 'Apex Legends'),
        ('Valorant', 'Valorant'),
        ('Fortnite', 'Fortnite'),
    ]
    game = forms.ChoiceField(choices=game_choices, label='Choose a game')

    class Meta:
        model = Profile
        fields = ['discord', 'steam', 'epic_games', 'age', 'game']

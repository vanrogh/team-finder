from django.contrib import admin
from .models import Profile, News

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'discord', 'steam', 'epic_games', 'age']
    search_fields = ['user__username', 'discord']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    search_fields = ['title', 'content']

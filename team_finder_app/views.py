from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import Profile, News
from .forms import ProfileForm


@login_required(login_url='/login/')
def home(request):
    return render(request, 'team_finder_app/home.html')

@login_required(login_url='/login/')
def search_teammates(request, game=None):
    if game is None:
        profiles = Profile.objects.all()
    else:
        profiles = Profile.objects.filter(game=game)
    games = sorted([game for game, _ in Profile.game_choices])
    return render(request, 'team_finder_app/search_teammates.html', {'profiles': profiles, 'game': game, 'games': games})

@login_required(login_url='/login/')
def news(request):
    news = News.objects.all()
    return render(request, 'team_finder_app/news.html', {'news': news})

@login_required(login_url='/login/')
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('game_profile', game=profile.game)
    else:
        form = ProfileForm()
    return render(request, 'team_finder_app/create_profile.html', {'form': form})

@login_required(login_url='/login/')
def game_profile(request, game):
    profiles = Profile.objects.filter(game=game)
    return render(request, 'team_finder_app/game_profile.html', {'profiles': profiles, 'game': game})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'team_finder_app/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'team_finder_app/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def chat_view(request):
    return render(request, 'team_finder_app/chat.html')
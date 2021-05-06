from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Player, Question
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
import random


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            player = Player.objects.create(user=user)

            player.save()

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {
        'form': form,
    })


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = 'game.html'


class LogoutView(LogoutView):
    success_url = 'login.html'


@login_required
def players(request):

    players_data = {'players': Player.objects.order_by('-total_score'),
                    'user': User.objects.get(id=request.user.id)}
    return render(request, 'players.html',
                  {'players_data': players_data})


@ login_required
@ csrf_exempt
def game_play(request):
    if request.method == "GET":

        questions = list(Question.objects.all())
        questions = random.sample(questions, 5 if len(
            questions) >= 5 else len(questions))

        game_data = {
            'player': Player.objects.get(user=request.user),
            'questions': questions
        }
        return render(request, 'game.html', {'game_data': game_data})
    elif request.method == "POST":

        player = Player.objects.get(user=request.user)

        player.total_score = int(request.POST.get('total_score'))
        player.games_played = int(request.POST.get('games_played'))

        player.save()

        return HttpResponse()

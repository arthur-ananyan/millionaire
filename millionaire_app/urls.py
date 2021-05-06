from django.urls import path
from .views import players, game_play, register, LoginView, LogoutView

urlpatterns = [
    path('', register, name="register"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('players/', players, name="players"),
    path('game/', game_play, name="game"),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

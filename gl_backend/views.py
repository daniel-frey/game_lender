from django.http import HttpResponse
from django.shortcuts import render

from gl_library.models import UserGameCopy


def home_view(request):
    """ view for homepage """

    random_game = UserGameCopy.objects.order_by('?').first()
    recent_games = UserGameCopy.objects.all().order_by('-id')[:10]
    other_random_games = UserGameCopy.objects.order_by('?')[:10]

    context = {
        'random_game': random_game,
        'recent_games': recent_games,
        'other_random_games': other_random_games
    }

    return render(request, 'base/home.html', context)

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import requests
import os
import json

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from gl_library.models import Game, Platform, UserGameCopy

from .forms import AddGameForm


def search_view(request):
    url = 'https://api-v3.igdb.com/games/'
    platforms_url = 'https://api-v3.igdb.com/platforms'

    if 'name' in request.GET:
        name = request.GET['name']
        search_payload = f'search "{name}";'
        headers = {
            'user-key': os.getenv('API_KEY')
        }
        r = requests.request("GET", url, data=search_payload, headers=headers)

        data = r.json()

        if data:
            context_dict = {}
            for i in range(len(data)):
                if i > 4:
                    break

                new_game = Game.objects.filter(game_id=data[i]["id"]).first()
                if new_game:
                    context_dict[i] = new_game

                else:
                    game_payload = f'''fields name,
                                         summary,
                                         platforms,
                                         cover.url,
                                         rating;
                                         where id = {data[i]["id"]};'''

                    req = requests.request("GET",
                                           url,
                                           data=game_payload,
                                           headers=headers)

                    api_data = req.json()

                    game = Game()
                    game.game_id = data[i]['id']
                    game.title = api_data[0].get('name')
                    game.description = api_data[0].get('summary')
                    game.cover_art = api_data[0].get('cover', {}).get('url')
                    game.aggregate_rating = api_data[0].get('rating')
                    game.save()

                    if api_data[0].get('platforms'):
                        for j in range(len(api_data[0].get('platforms'))):
                            platform = Platform.objects.filter(igdb_platform_id=api_data[0]['platforms'][j]).first()
                            if not platform:
                                platform_payload = f'fields name; where id = {api_data[0]["platforms"][j]};'
                                new_platform = requests.request("GET", platforms_url, data=platform_payload, headers=headers)
                                platform_data = new_platform.json()

                                platform = Platform()
                                platform.igdb_platform_id = api_data[0]['platforms'][j]
                                platform.platform_name = platform_data[0].get('name')
                                platform.save()

                        for k in range(len(api_data[0].get('platforms'))):
                            game_platform = Platform.objects.filter(igdb_platform_id=api_data[0]['platforms'][k]).first()
                            game.platforms.add(game_platform)

                    context_dict[i] = game

            context = {'games': context_dict}
            return render(request, 'search.html', context)

    return render(request, 'search.html')


class AddGameView(LoginRequiredMixin, FormView):
    """
    POST /search/addgame/
        add game with game id and platform
    """

    template_name = 'search.html'
    form_class = AddGameForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('game_list_view')

    def post(self, request, *args, **kwargs):
        game_id = request.POST['game_id']
        game = Game.objects.filter(id=game_id).first()
        platform_id = request.POST['platforms']
        platform = Platform.objects.filter(igdb_platform_id=platform_id).first()

        existing_game = UserGameCopy.objects.filter(
            owner=request.user,
            game=game,
            platform=platform
        ).first()

        if existing_game:
            messages.info(self.request, 'That game is already in your library')
            return redirect('own_game_list_view')

        game_copy = UserGameCopy(
            owner=request.user,
            game=game,
            platform=platform,
            checked_out_user=request.user
        )
        game_copy.save()

        messages.info(self.request, 'Added to your library!')
        return redirect('own_game_list_view')

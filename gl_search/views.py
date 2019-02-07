from django.shortcuts import render
import requests
import os
import json

from gl_library.models import Game, Platform


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
            print('data length:', len(data))
            for i in range(len(data)):
                if i > 4:
                    break

                new_game = Game.objects.filter(game_id=data[i]["id"]).first()
                if new_game:
                    print(new_game.title)
                    context_dict[i] = {
                        'name': new_game.title,
                        'summary': new_game.description,
                        'cover': new_game.cover_art,
                        'rating': new_game.aggregate_rating,
                    }

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

                    if api_data[0].get('platforms'):
                        for i in range(len(api_data[0].get('platforms'))):
                            platform = Platform.objects.filter(igdb_platform_id=api_data[0]['platforms'][i]).first()
                            if not platform:
                                platform_payload = f'fields name; where id = {api_data[0]["platforms"][i]};'
                                new_platform = requests.request("GET", platforms_url, data=platform_payload, headers=headers)
                                platform_data = new_platform.json()

                                new_db_platform = Platform()
                                new_db_platform.igdb_platform_id = api_data[0]['platforms'][i]
                                new_db_platform.platform_name = platform_data[0].get('name')
                                new_db_platform.save()

                        platforms = []
                        for i in range(len(api_data[0].get('platforms'))):
                            game_platform = Platform.objects.filter(igdb_platform_id=api_data[0]['platforms'][i]).first()
                            platforms.append(game_platform.platform_name)

                    print(platforms)
                    context_dict[i] = {
                        'name': api_data[0].get('name'),
                        'summary': api_data[0].get('summary'),
                        'cover': api_data[0].get('cover', {}).get('url'),
                        'rating': api_data[0].get('rating'),
                    }

                    game = Game()
                    game.game_id = data[i]['id']
                    game.title = api_data[0].get('name')
                    game.description = api_data[0].get('summary')
                    game.cover_art = api_data[0].get('cover', {}).get('url')
                    game.aggregate_rating = api_data[0].get('rating')
                    game.save()

            context = {'games': context_dict}
            print(context)
            return render(request, 'search.html', context)

    return render(request, 'search.html')

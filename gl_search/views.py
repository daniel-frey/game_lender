from django.shortcuts import render
import requests
import os
import json


def search_view(request):
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://api-v3.igdb.com/games/'
        payload = f'fields name, cover.url, rating; where name ~ "{name}";'
        headers = {
            'user-key': os.getenv('API_KEY')
        }
        r = requests.request("GET", url, data=payload, headers=headers)

        data = r.json()

        if data:
            context = {
                'name': data[0]['name'],
                'cover': data[0]['cover']['url'],
                'rating': data[0]['rating'],
            }
            return render(request, 'search.html', context)

    return render(request, 'search.html')

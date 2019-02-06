from django.shortcuts import render
import requests
import os
import json


def search_view(request):
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://api-v3.igdb.com/games/'
        payload = f'search "{name}";'
        headers = {
            'user-key': os.getenv('API_KEY')
        }
        r = requests.request("GET", url, data=payload, headers=headers)

        data = r.json()

        if data:
            context = {}
            for i in range(len(data)):
                payload = f'fields name, cover.url, rating; where id = {data[i]["id"]};'
                req = requests.request("GET", url, data=payload, headers=headers)
                api_data = req.json()
                context_dict = {
                    'name': api_data[0]['name'],
                    'cover': api_data[0]['cover']['url'],
                    'rating': api_data[0]['rating'],
                }

                context[i] = context_dict
            print(context)
            return render(request, 'search.html', context)

    return render(request, 'search.html')

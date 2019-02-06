from django.contrib import admin

from .models import Game, UserGameCopy

admin.site.register((Game, UserGameCopy))

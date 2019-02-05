from django.contrib import admin

from .models import Game, GameStatus

admin.site.register((Game, GameStatus))

from django.contrib import admin

from .models import Game, UserGameCopy, BorrowEvent

admin.site.register((Game, UserGameCopy, BorrowEvent))

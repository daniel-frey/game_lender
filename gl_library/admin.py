from django.contrib import admin

from .models import Game, UserGameCopy, BorrowEvent, Platform

admin.site.register((Game, UserGameCopy, BorrowEvent, Platform))

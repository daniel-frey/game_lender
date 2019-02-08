from .views import search_view, AddGameView
from django.urls import path


urlpatterns = [
    path('', search_view, name='search_view'),
    path('addgame', AddGameView.as_view(), name='add_game_view')
]

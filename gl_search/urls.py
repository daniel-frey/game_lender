from .views import search_view
from django.urls import path


urlpatterns = [
    path('', search_view, name='search_view'),
]

from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    """ view for homepage """
    return render(request, 'base/home.html')

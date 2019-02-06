
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Game, UserGameCopy, BorrowEvent


class UserGameCopyList(LoginRequiredMixin, ListView):
    """
    GET /library/
        view a user's library, own or other
    POST /library/<id>
        add new game to user's own list.
    """
    template_name = 'user_game_list.html'
    model = UserGameCopy
    context_object_name = 'games'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return UserGameCopy.objects.filter(owner__id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = User.objects.filter(id=self.kwargs.get('id'))[0]
        context['games'] = UserGameCopy.objects.filter(owner__id=self.kwargs.get('id'))
        return context


class UserGameCopyDetailView(LoginRequiredMixin, DetailView):
    """
    GET /library/details/<id>
        get details for specific instance of a user game
    """
    template_name = 'user_game_detail.html'
    model = UserGameCopy
    context_object_name = 'games'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return UserGameCopy.objects.filter(id=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = UserGameCopy.objects.filter(id=self.kwargs.get('pk'))[0]
        return context


# class BorrowConfirmation(LoginRequiredMixin, View):
#     """
#     GET /library/borrow/<id>
#         checks if game is available, brings up screen asking user for confirm
#         if they want to borrow.
#     POST /library/borrow/<id>
#         checks if game is available and makes request to borrow it
#     """
#     template_name = 'borrow_confirmation.html'
#     login_url = reverse_lazy('login')

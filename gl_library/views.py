
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

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

    def get_context_data(self, **kwargs):
        if self.kwargs.get('id'):
            user_id = self.kwargs.get('id')
        else:
            user_id = self.request.user.id
        owner = get_object_or_404(User, id=user_id)
        context = super().get_context_data(**kwargs)
        context['owner'] = owner
        context['games'] = UserGameCopy.objects.filter(owner=owner)
        return context


class UserGameCopyDetailView(LoginRequiredMixin, DetailView):
    """
    GET /library/details/<id>
        get details for specific instance of a user game
    """
    template_name = 'user_game_detail.html'
    model = UserGameCopy
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = get_object_or_404(UserGameCopy, id=self.kwargs.get('pk'))
        context['game'] = game
        return context


class BorrowConfirmation(LoginRequiredMixin, TemplateView):
    """
    GET /library/borrow/<id>
        checks if game is available, brings up screen asking user for confirm
        if they want to borrow.
    POST /library/borrow/<id>
        checks if game is available and makes request to borrow it
    """
    template_name = 'borrow_confirmation.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = get_object_or_404(UserGameCopy, id=self.kwargs.get('pk'))
        context['game'] = game
        return context

    def post(self, request, *args, **kwargs):
        game = get_object_or_404(UserGameCopy, id=self.kwargs.get('pk'))
        if BorrowEvent.objects.filter(borrower=request.user, status='pending').first():
            messages.info(request, f'You\'ve already requested to borrow this game.')
            return redirect('own_game_list_view')

        borrow_event = BorrowEvent(
            game=game,
            borrower=request.user,
        )
        borrow_event.save()

        messages.info(request, f'You have requested {game.game.title} from {game.owner}\'s library.')
        return redirect('own_game_list_view')


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    GET /profile/
        lists user's own profile:
            games they've borrowed
            pending borrows on their games
            pending borrows they've made
            last 5 events (not pending)
    """
    template_name = 'profile.html'
    login_url = reverse_lazy('login')


from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
from django.utils import timezone


from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)

from .models import Game, UserGameCopy, BorrowEvent
from gl_messages.models import Message


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
        if BorrowEvent.objects.filter(borrower=request.user, status='pending', game=game).first():
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['borrowing_games'] = UserGameCopy.objects.filter(status='out', checked_out_user=self.request.user)
        context['lending_games'] = UserGameCopy.objects.filter(status='out', owner=self.request.user)
        context['incoming_borrow_requests'] = BorrowEvent.objects.filter(game__owner=self.request.user, status='pending')
        context['outgoing_borrow_requests'] = BorrowEvent.objects.filter(borrower=self.request.user, status='pending')
        context['request_history'] = BorrowEvent.objects.filter(game__owner=self.request.user).exclude(status='pending')[:5]
        context['user_messages'] = Message.objects.filter(to_user__id=self.request.user.id, read=False)[:5]

        return context


# These views are not assigned to particular pages, these are just the controllers for borrow operations


def accept_request_view(request):
    """ when user accepts a request """
    borrow_request_id = request.POST.get('request')
    borrow_request = BorrowEvent.objects.filter(id=borrow_request_id).first()

    if request.user != borrow_request.game.owner:
        messages.info(request, f'You\'re not authorized to accept that request.')
        return redirect('profile_view')

    borrow_request.status = 'approved'
    borrow_request.save()

    game = borrow_request.game
    game.status = 'out'
    game.checked_out_user = borrow_request.borrower
    game.checked_out_date = timezone.now()
    game.save()

    messages.info(request, f'You have accepted {borrow_request.borrower.username}\'s request to borrow {borrow_request.game.game.title}.')
    return redirect('profile_view')


def deny_request_view(request):
    """ when user denies a request """
    borrow_request_id = request.POST.get('request')
    borrow_request = BorrowEvent.objects.filter(id=borrow_request_id).first()

    if request.user != borrow_request.game.owner:
        messages.info(request, f'You\'re not authorized to deny that request.')
        return redirect('profile_view')

    borrow_request.status = 'denied'
    borrow_request.save()

    messages.info(request, f'You have denied {borrow_request.borrower.username}\'s request to borrow {borrow_request.game.game.title}.')
    return redirect('profile_view')


def mark_as_returned_view(request):
    """ when user marks a game they've loaned as returned """
    loaned_game_id = request.POST.get('game_id')
    loaned_game = UserGameCopy.objects.filter(id=loaned_game_id).first()

    if loaned_game.owner != request.user:
        messages.info(request, f'You are not authorized to mark that game as returned.')
        return redirect('profile_view')

    borrow_request = BorrowEvent.objects.filter(game=loaned_game).first()
    borrow_request.status = 'complete'
    borrow_request.save()
    loaned_game.status = 'in'
    loaned_game.save()

    messages.info(request, f'You have marked {loaned_game.game.title} as returned.')
    return redirect('profile_view')

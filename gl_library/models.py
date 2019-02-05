from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Game(models.Model):
    """ this is the data saved about a particular game - cover art, name,
    etc. not unique to a user's specific copy of a game.

    game_id
    name
    cover_art
    rating
    """

    game_id = models.IntegerField()
    title = models.CharField(max_length=96)
    cover_art = models.CharField(max_length=1028)
    rating = models.FloatField()

    def __str__(self):
        return f'Game: {self.title}'


class GameStatus(models.Model):
    """ model for a unique game in a user's library. Includes info about
    status, who's checking it out, when it's due back

    game (reference to game model)
    status
    checked_out_date
    checked_out_user (reference to user model)
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='game_statuses_owner',
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='game_statuses_game'
    )

    statuses = [
        ('out', 'Checked Out'),
        ('in', 'Checked In')
    ]

    status = models.CharField(
        max_length=96,
        choices=statuses,
        default='in'
    )

    checked_out_date = models.DateTimeField(default=timezone.now)

    checked_out_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='game_statuses_checkout_user',
        default='hello'
    )

    def __str__(self):
        return f'{self.owner}\'s {self.game.title}'

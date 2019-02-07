from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Platform(models.Model):
    """ this is just a k:v storage of platform id:platform string """
    igdb_platform_id = models.IntegerField()
    platform_name = models.CharField(max_length=96)


class Game(models.Model):
    """ this is the data saved about a particular game - cover art, name,
    etc. not unique to a user's specific copy of a game.

    game_id
    title
    description
    cover_art
    aggregate_rating
    """

    game_id = models.IntegerField(null=True)
    title = models.CharField(max_length=96, null=True)
    cover_art = models.CharField(max_length=1028, null=True)
    description = models.TextField(null=True)

    platform = models.ForeignKey(
        Platform,
        on_delete=models.CASCADE,
        related_name='game_platform',
        null=True
    )

    aggregate_rating = models.FloatField(null=True)

    def __str__(self):
        return f'Game: {self.title}'


class UserGameCopy(models.Model):
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
        null=True
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='game_statuses_game',
        null=True
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
        null=True
    )

    def __str__(self):
        return f'{self.owner}\'s {self.game.title}'


class BorrowEvent(models.Model):
    """ model for an event of a user making a borrow request

    game (reference to UserGameCopy model)
    borrower (reference to User model)
    request_date
    status
    """

    game = models.ForeignKey(
        UserGameCopy,
        on_delete=models.CASCADE,
        related_name='borrowed_game',
        null=True
    )

    borrower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='game_borrower',
        null=True
    )

    request_date = models.DateTimeField(default=timezone.now)

    statuses = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
        ('complete', 'Complete')
    ]

    status = models.CharField(
        max_length=96,
        choices=statuses,
        default='pending'
    )

    @property
    def lender(self):
        return self.game.owner

    def __str__(self):
        return f'Borrow Event: {self.borrower} borrows {self.lender}\'s {self.game.game.title}'

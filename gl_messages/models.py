from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    """ model for a message from a user to another user """

    from_user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        related_name='message_from',
        null=True,
        default=None
    )

    to_user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        related_name='message_to',
        null=True,
        default=None
    )

    subject = models.CharField(max_length=1028)
    body = models.TextField()

    sent_date = models.DateTimeField(default=timezone.now)

    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.from_user} to {self.to_user}: {self.subject}'

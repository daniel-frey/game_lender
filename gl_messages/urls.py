from django.urls import path
from .views import (
    MessageInboxView,
    MessageDetailView,
    SendMessageView
)

urlpatterns = [
    path('', MessageInboxView.as_view(), name='inbox_view'),
    path('details/<int:pk>/', MessageDetailView.as_view(), name='message_detail_view'),
    path('send/', SendMessageView.as_view(), name='send_message_view'),
    path('send/<int:pk>/', SendMessageView.as_view(), name='reply_message_view')
]

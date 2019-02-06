from django.urls import path
from .views import (
    UserGameCopyList,
    UserGameCopyDetailView,
    # BorrowConfirmation
)

urlpatterns = [
    path('<int:id>', UserGameCopyList.as_view(), name='game_list_view'),
    path('details/<int:pk>', UserGameCopyDetailView.as_view(), name='game_detail_view')
]

from django.urls import path
from .views import (
    UserGameCopyList,
    UserGameCopyDetailView,
    BorrowConfirmation
)

urlpatterns = [
    path('', UserGameCopyList.as_view(), name='own_game_list_view'),
    path('<int:id>', UserGameCopyList.as_view(), name='game_list_view'),
    path('details/<int:pk>', UserGameCopyDetailView.as_view(), name='game_detail_view'),
    path('borrow/<int:pk>', BorrowConfirmation.as_view(), name='borrow_confirmation_view')
]

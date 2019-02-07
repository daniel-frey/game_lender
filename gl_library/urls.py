from django.urls import path
from .views import (
    UserGameCopyList,
    UserGameCopyDetailView,
    BorrowConfirmation,
    ProfileView,
    accept_request_view,
    deny_request_view,
    mark_as_returned_view
)

urlpatterns = [
    path('', UserGameCopyList.as_view(), name='own_game_list_view'),
    path('<int:id>', UserGameCopyList.as_view(), name='game_list_view'),
    path('details/<int:pk>', UserGameCopyDetailView.as_view(), name='game_detail_view'),
    path('borrow/<int:pk>', BorrowConfirmation.as_view(), name='borrow_confirmation_view'),
    path('profile', ProfileView.as_view(), name='profile_view'),
    path('accept', accept_request_view, name='accept_request_view'),
    path('deny', deny_request_view, name='deny_request_view'),
    path('return', mark_as_returned_view, name='mark_as_returned_view')
]

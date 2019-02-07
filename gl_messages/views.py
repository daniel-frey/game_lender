from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Message
from .forms import MessageForm


class MessageInboxView(LoginRequiredMixin, ListView):
    """
    GET /messages/
        user views their inbox.
    """
    template_name = 'inbox.html'
    model = Message
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.GET.get('page'):
            page = 1
        else:
            page = self.request.GET.get('page')

        messages_all = Message.objects.filter(to_user__id=self.request.user.id)
        paginator = Paginator(messages_all, 20)
        user_messages = paginator.get_page(page)

        context['user_messages'] = user_messages
        return context


class MessageDetailView(LoginRequiredMixin, DetailView):
    """
    GET /messages/<pk>
        user views details of specific message pk
    """
    template_name = 'message_detail.html'
    model = Message
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        message_id = self.kwargs.get('pk')
        user_message = get_object_or_404(Message, id=message_id, to_user=self.request.user)

        if user_message.read is False:
            user_message.read = True
            user_message.save()

        context['user_message'] = user_message
        return context


class SendMessageView(LoginRequiredMixin, FormView):
    """
    GET /messages/send/
        user visits send message page (not replying)
    GET /messages/send/<pk>
        user is replying to message pk (must be recipient of pk)
    POST /messages/send/
        user is sending a message.
    """
    template_name = 'send.html'
    context_object_name = 'user_message'
    form_class = MessageForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('inbox_view')

    def user_message(self):
        if self.kwargs.get('pk'):
            message_id = self.kwargs.get('pk')
            user_message = get_object_or_404(Message, id=message_id, to_user=self.request.user)
            return user_message

    def form_valid(self, form):
        to_username = form.data['to_user']
        to_user = User.objects.filter(username=to_username).first()
        subject = form.data['subject']
        body = form.data['body']

        if to_user:
            user_message = Message(
                from_user=self.request.user,
                to_user=to_user,
                subject=subject,
                body=body
            )
            user_message.save()
            messages.info(self.request, 'Message sent!')
            return redirect('inbox_view')

        messages.info(self.request, 'that user doesnt exist')
        return redirect('send_message_view')

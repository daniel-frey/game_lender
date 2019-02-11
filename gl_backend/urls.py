from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('search/', include('gl_search.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('library/', include('gl_library.urls')),
    path('messages/', include('gl_messages.urls'))
]

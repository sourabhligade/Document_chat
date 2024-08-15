from django.urls import path
from .views import start_chat, send_message, chat_history

urlpatterns = [
    path('start/', start_chat, name='start_chat'),
    path('message/', send_message, name='send_message'),
    path('history/<str:chat_thread_id>/', chat_history, name='chat_history'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"chats//$",ChatConsumer.as_asgi()),
]
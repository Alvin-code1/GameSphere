from django.urls import path
from . import views

urlpatterns = [
    path('api/chats/',views.ChatAPIView.as_view(),name='Chats'),
    path('api/chats/<int:pk>/',views.ChatAPIView.as_view(),name='Chats'),
    path('api/messaage/',views.MessageAPIView.as_view(),name='Message'),
    path('api/messaage/<int:pk>/',views.MessageAPIView.as_view(),name='Message')
]
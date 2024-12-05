from django.urls import path
from . import views

urlpatterns = [
    path('api/profile/',views.ProfileAPIView.as_view(),name='Profile'),
    path('api/profile/<int:pk>/',views.ProfileAPIView.as_view(),name='Profile'),
]
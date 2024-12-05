from django.urls import path
from . import views

urlpatterns = [
    path('api/post/',views.PostAPIView.as_view(),name='Post'),
    path('api/post/<int:pk>/',views.PostAPIView.as_view(),name='Post'),
]
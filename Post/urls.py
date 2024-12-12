from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.handle_post_request, name='handle_post_request'),
    path('posts/reaction/', views.modify_reaction_count, name='modify_reaction_count'),
]

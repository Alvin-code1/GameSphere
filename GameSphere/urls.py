from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('accounts/',include('allauth.urls')),
    re_path('profile/',include('Profile.urls')),
    re_path('post/',include('Post.urls')),
    re_path('chats/',include('Chats.urls')),
    re_path('groups/',include('Groups.urls')),
]

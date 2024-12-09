from django.urls import path
from . import views

urlpatterns = [
    path('api/groups/',views.GroupAPIView.as_view(),name='Post'),
    path('api/groups/<int:_pk>/',views.GroupAPIView.as_view(),name='Post'),
]
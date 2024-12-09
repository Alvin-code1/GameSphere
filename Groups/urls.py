from django.urls import path
from . import views

urlpatterns = [
    path('',views.GroupAPIView.as_view(),name='Post'),
    path('<int:_pk>/',views.GroupAPIView.as_view(),name='Post'),
]
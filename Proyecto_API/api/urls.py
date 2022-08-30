from django.urls import path
from .views import VideoViews

urlpatterns = [
    path('companies/', VideoViews.as_view(), name='video_list'),
    path('companies/<int:id>', VideoViews.as_view(), name='video_process')
]
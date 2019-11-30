from django.urls import path

from video_rtmp.views import video_view

urlpatterns = [
    path('youke/<video_url>/', video_view,name='yzs'),
]
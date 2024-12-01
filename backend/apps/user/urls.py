from django.urls import path
from .views import UserInfoView, RoadMap_Motivation

app_name = 'user'

urlpatterns = [
    path('info', UserInfoView.as_view(), name='info'),
    path('roadmap-motivation/', RoadMap_Motivation.as_view(),
         name='roadmap_motivation'),
]

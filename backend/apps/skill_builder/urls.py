from django.urls import path
from .views import TopicFatherListView, check_spelling

app_name = 'skill_builder'

urlpatterns = [
    path('topics/', TopicFatherListView.as_view(), name='topic-father-list'),
    path('check_spelling/', check_spelling, name='check_spelling'),
]



from django.urls import path
from .views import TopicFatherListView, check_spelling, CreateTableForm03View, save_sentences, CrearOracionView, RevisarTraduccionView

app_name = 'skill_builder'

urlpatterns = [
    path('topics/', TopicFatherListView.as_view(), name='topic-father-list'),
    path('check_spelling/', check_spelling, name='check_spelling'),
    path('create/', CreateTableForm03View.as_view(), name='create_form'),
    path('save_sentences/', save_sentences, name='save_sentences'),
    path('crear-oracion/', CrearOracionView.as_view(), name='crear_oracion'),
    path('revisar-traduccion/', RevisarTraduccionView.as_view(),
         name='revisar_traduccion'),

]

from django.urls import path
from .views import (
    CrearOracionView, RevisarTraduccionView, TitleDetailView, TableForm03ListView,
    check_answer, NivelesListView, ContenidosListView, TemasListView
)

app_name = 'skill_practice'

urlpatterns = [
    path('tableform03/', TableForm03ListView.as_view(), name='tableform03-list'),
    path('practice/<int:pk>/', TitleDetailView.as_view(), name='title-detail'),
    path('check_answer/', check_answer, name='check-answer'),
    path('crear-oracion/', CrearOracionView.as_view(), name='crear_oracion'),
    path('revisar-traduccion/', RevisarTraduccionView.as_view(),
         name='revisar_traduccion'),
    path('niveles/', NivelesListView.as_view(), name='niveles-list'),
    path('contenidos/', ContenidosListView.as_view(), name='contenidos-list'),
    path('temas/', TemasListView.as_view(), name='temas-list'),

]

from django.urls import path
from .views import GenreListView, GenreDetailView

app_name = 'webapp'

urlpatterns = [
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail')
]
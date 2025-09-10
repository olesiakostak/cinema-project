from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genres/add/', views.GenreCreateView.as_view(), name='genre-add'),
    path('genres/update/<int:pk>/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genres/delete/<int:pk>/', views.GenreDeleteView.as_view(), name='genre-delete'),
    path('films/', views.FilmListView.as_view(), name='film-list'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film-detail')
]
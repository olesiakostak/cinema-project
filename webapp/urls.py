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
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film-detail'),
    path('films/add/', views.FilmCreateView.as_view(), name='film-add'),
    path('films/update/<int:pk>/', views.FilmUpdateView.as_view(), name='film-update'),
    path('film/delete/<int:pk>/', views.FilmDeleteView.as_view(), name='film-delete'),

    path('halls/', views.HallListView.as_view(), name='hall-list'),
    path('halls/<int:pk>/', views.HallDetailView.as_view(), name='hall-detail'),
    path('halls/add/', views.HallCreateView.as_view(), name='hall-add'),
    path('halls/update/<int:pk>/', views.HallUpdateView.as_view(), name='hall-update'),
    path('halls/delete/<int:pk>/', views.HallDeleteView.as_view(), name='hall-delete'),

    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    path('customers/update/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer-delete')
]
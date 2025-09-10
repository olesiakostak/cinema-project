from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Genre, Film


class GenreListView(ListView):
    template_name = 'webapp/genre_list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return unit_of_work.genres.get_all()

class GenreDetailView(DetailView):
    template_name = 'webapp/genre_detail.html'
    context_object_name = 'genre'

    def get_queryset(self):
        return unit_of_work.genres.get_all()
    
class GenreCreateView(CreateView):
    model = Genre
    fields = ['name']
    template_name = 'webapp/genre_form.html'
    success_url = reverse_lazy('webapp:genre-list')

class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name']
    template_name = 'webapp/genre_form.html'
    success_url = reverse_lazy('webapp:genre-list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'webapp/genre_confirm_delete.html'
    success_url = reverse_lazy('webapp:genre-list')


class FilmListView(ListView):
    template_name = 'webapp/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        return unit_of_work.films.get_all()
    
class FilmDetailView(DetailView):
    template_name = 'webapp/film_detail.html'
    context_object_name = 'film'

    def get_queryset(self):
        return unit_of_work.films.get_all()
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Genre


class GenreListView(ListView):
    template_name = 'webapp/genre/list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return unit_of_work.genres.get_all()

class GenreDetailView(DetailView):
    template_name = 'webapp/genre/detail.html'
    context_object_name = 'genre'

    def get_queryset(self):
        return unit_of_work.genres.get_all()
    
class GenreCreateView(CreateView):
    model = Genre
    fields = ['name']
    template_name = 'webapp/genre/form.html'
    success_url = reverse_lazy('webapp:genre-list')

class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name']
    template_name = 'webapp/genre/form.html'
    success_url = reverse_lazy('webapp:genre-list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'webapp/genre/confirm_delete.html'
    success_url = reverse_lazy('webapp:genre-list')
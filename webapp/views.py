from django.views.generic import ListView
from django.views.generic import DetailView
from app.catalog.repositories import unit_of_work


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

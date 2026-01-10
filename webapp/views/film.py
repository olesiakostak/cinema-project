from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy, reverse
from app.catalog.models import Film
from ..forms import FilmForm

class FilmListView(ListView):
    template_name = 'webapp/film/list.html'
    context_object_name = 'films'

    def get_queryset(self):
        return unit_of_work.films.get_all()
    
class FilmDetailView(DetailView):
    template_name = 'webapp/film/detail.html'
    context_object_name = 'film'

    def get_queryset(self):
        return unit_of_work.films.get_all()
    
class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'webapp/film/form.html'
    success_url = reverse_lazy('webapp:film-list')

class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'webapp/film/form.html'
    
    def get_success_url(self):
        return reverse('webapp:film-detail', kwargs={'pk': self.object.pk})

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'webapp/film/confirm_delete.html'
    success_url = reverse_lazy('webapp:film-list')



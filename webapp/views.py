from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Genre, Film, Hall, Customer
from .forms import FilmForm


class GenreListView(ListView):
    template_name = 'webapp/genre/genre_list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return unit_of_work.genres.get_all()

class GenreDetailView(DetailView):
    template_name = 'webapp/genre/genre_detail.html'
    context_object_name = 'genre'

    def get_queryset(self):
        return unit_of_work.genres.get_all()
    
class GenreCreateView(CreateView):
    model = Genre
    fields = ['name']
    template_name = 'webapp/genre/genre_form.html'
    success_url = reverse_lazy('webapp:genre-list')

class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name']
    template_name = 'webapp/genre/genre_form.html'
    success_url = reverse_lazy('webapp:genre-list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'webapp/genre/genre_confirm_delete.html'
    success_url = reverse_lazy('webapp:genre-list')


class FilmListView(ListView):
    template_name = 'webapp/film/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        return unit_of_work.films.get_all()
    
class FilmDetailView(DetailView):
    template_name = 'webapp/film/film_detail.html'
    context_object_name = 'film'

    def get_queryset(self):
        return unit_of_work.films.get_all()
    
class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'webapp/film/film_form.html'
    success_url = reverse_lazy('webapp:film-list')

class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'webapp/film/film_form.html'
    success_url = reverse_lazy('webapp:film-list')

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'webapp/film/film_confirm_delete.html'
    success_url = reverse_lazy('webapp:film-list')

class HallListView(ListView):
    template_name = 'webapp/hall/hall_list.html'
    context_object_name = 'halls'

    def get_queryset(self):
        return unit_of_work.halls.get_all()

class HallDetailView(DetailView):
    template_name = 'webapp/hall/hall_detail.html'
    context_object_name = 'hall'

    def get_queryset(self):
        return unit_of_work.halls.get_all()
    
class HallCreateView(CreateView):
    model = Hall
    fields = ['name', 'screen_type']
    template_name = 'webapp/hall/hall_form.html'
    success_url = reverse_lazy('webapp:hall-list')

class HallUpdateView(UpdateView):
    model = Hall
    fields = ['name', 'screen_type']
    template_name = 'webapp/hall/hall_form.html'
    success_url = reverse_lazy('webapp:hall-list')

class HallDeleteView(DeleteView):
    model = Hall
    template_name = 'webapp/hall/hall_confirm_delete.html'
    success_url = reverse_lazy('webapp:hall-list')

class CustomerListView(ListView):
    template_name = 'webapp/customer/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return unit_of_work.customers.get_all()

class CustomerDetailView(DetailView):
    template_name = 'webapp/customer/customer_detail.html'
    context_object_name = 'customer'

    def get_queryset(self):
        return unit_of_work.customers.get_all()
    
class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date']
    template_name = 'webapp/customer/customer_form.html'
    success_url = reverse_lazy('webapp:customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date']
    template_name = 'webapp/customer/customer_form.html'
    success_url = reverse_lazy('webapp:customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'webapp/customer/customer_confirm_delete.html'
    success_url = reverse_lazy('webapp:customer-list')

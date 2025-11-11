from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Seat

class SeatListView(ListView):
    template_name = 'webapp/seat/list.html'
    context_object_name = 'seats'

    def get_queryset(self):
        return unit_of_work.seats.get_all()

class SeatDetailView(DetailView):
    template_name = 'webapp/seat/detail.html'
    context_object_name = 'seat'

    def get_queryset(self):
        return unit_of_work.seats.get_all()
    
class SeatCreateView(CreateView):
    model = Seat
    fields = ['hall', 'row', 'seat']
    template_name = 'webapp/seat/form.html'
    success_url = reverse_lazy('webapp:seat-list')

class SeatUpdateView(UpdateView):
    model = Seat
    fields = ['hall', 'row', 'seat']
    template_name = 'webapp/seat/form.html'
    success_url = reverse_lazy('webapp:seat-list')

class SeatDeleteView(DeleteView):
    model = Seat
    template_name = 'webapp/seat/confirm_delete.html'
    success_url = reverse_lazy('webapp:seat-list')
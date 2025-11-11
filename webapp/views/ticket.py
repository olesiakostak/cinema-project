from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Ticket

class TicketListView(ListView):
    template_name = 'webapp/ticket/list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return unit_of_work.tickets.get_all()

class TicketDetailView(DetailView):
    template_name = 'webapp/ticket/detail.html'
    context_object_name = 'ticket'

    def get_queryset(self):
        return unit_of_work.tickets.get_all()
    
class TicketCreateView(CreateView):
    model = Ticket
    fields = ['session', 'seat', 'base_price', 'status']
    template_name = 'webapp/ticket/form.html'
    success_url = reverse_lazy('webapp:ticket-list')

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ['session', 'seat', 'base_price', 'status']
    template_name = 'webapp/ticket/form.html'
    success_url = reverse_lazy('webapp:ticket-list')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'webapp/ticket/confirm_delete.html'
    success_url = reverse_lazy('webapp:ticket-list')
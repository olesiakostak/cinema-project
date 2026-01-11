from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from app.catalog.models import Session, Seat, Ticket
from ..forms import SessionForm
from django.utils import timezone

class SessionListView(ListView):
    template_name = 'webapp/session/list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        return unit_of_work.sessions.get_all()

class SessionDetailView(DetailView):
    template_name = 'webapp/session/detail.html'
    context_object_name = 'session'

    def get_queryset(self):
        return unit_of_work.sessions.get_all()
    
class SessionCreateView(CreateView):
    model = Session
    form_class = SessionForm
    template_name = 'webapp/session/form.html'
    success_url = reverse_lazy('webapp:session-list')

class SessionUpdateView(UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'webapp/session/form.html'
    success_url = reverse_lazy('webapp:session-list')

class SessionDeleteView(DeleteView):
    model = Session
    template_name = 'webapp/session/confirm_delete.html'
    success_url = reverse_lazy('webapp:session-list')

class BookingView(ListView):
    template_name = 'webapp/session/booking.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        return unit_of_work.sessions.get_all().filter(
            start_time__gt=timezone.now()
        )

class BookingDetailView(DetailView):
    model = Session
    template_name = 'webapp/session/booking_detail.html'
    context_object_name = 'session'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_seats'] = Seat.objects.filter(hall = self.object.hall)
        context['booked_tickets'] = Ticket.objects.filter(
            session = self.object, 
            status__in = [Ticket.Status.BOOKED, Ticket.Status.SOLD]
        ).values_list('seat_id', flat=True)
        return context
    
def CreateBooking(request, session_id, seat_id):

    session = get_object_or_404(Session, pk=session_id)
    seat = get_object_or_404(Seat, pk=seat_id)

    if Ticket.objects.filter(session=session, seat=seat).exists():
        return redirect('webapp:booking-detail', pk=session_id)

    new_ticket = Ticket.objects.create(
        session=session,
        seat=seat,
        status=Ticket.Status.BOOKED,
        base_price=150.00  
    )

    return redirect('webapp:ticket-detail', pk=new_ticket.id)
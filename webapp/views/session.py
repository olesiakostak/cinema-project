from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Session
from ..forms import SessionForm

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
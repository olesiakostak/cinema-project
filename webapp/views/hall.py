from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Hall

class HallListView(ListView):
    template_name = 'webapp/hall/list.html'
    context_object_name = 'halls'

    def get_queryset(self):
        return unit_of_work.halls.get_all()

class HallDetailView(DetailView):
    template_name = 'webapp/hall/detail.html'
    context_object_name = 'hall'

    def get_queryset(self):
        return unit_of_work.halls.get_all()
    
class HallCreateView(CreateView):
    model = Hall
    fields = ['name', 'screen_type']
    template_name = 'webapp/hall/form.html'
    success_url = reverse_lazy('webapp:hall-list')

class HallUpdateView(UpdateView):
    model = Hall
    fields = ['name', 'screen_type']
    template_name = 'webapp/hall/form.html'
    success_url = reverse_lazy('webapp:hall-list')

class HallDeleteView(DeleteView):
    model = Hall
    template_name = 'webapp/hall/confirm_delete.html'
    success_url = reverse_lazy('webapp:hall-list')

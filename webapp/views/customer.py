from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Customer


class CustomerListView(ListView):
    template_name = 'webapp/customer/list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return unit_of_work.customers.get_all()

class CustomerDetailView(DetailView):
    template_name = 'webapp/customer/detail.html'
    context_object_name = 'customer'

    def get_queryset(self):
        return unit_of_work.customers.get_all()
    
class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date']
    template_name = 'webapp/customer/form.html'
    success_url = reverse_lazy('webapp:customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date']
    template_name = 'webapp/customer/form.html'
    success_url = reverse_lazy('webapp:customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'webapp/customer/confirm_delete.html'
    success_url = reverse_lazy('webapp:customer-list')

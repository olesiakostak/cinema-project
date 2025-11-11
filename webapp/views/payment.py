from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import Payment


class PaymentListView(ListView):
    template_name = 'webapp/payment/list.html'
    context_object_name = 'payments'

    def get_queryset(self):
        return unit_of_work.payments.get_all()

class PaymentDetailView(DetailView):
    template_name = 'webapp/payment/detail.html'
    context_object_name = 'payment'

    def get_queryset(self):
        return unit_of_work.payments.get_all()
    
class PaymentCreateView(CreateView):
    model = Payment
    fields = ['customer', 'ticket', 'gift_certificate', 'status', 'operation_type']
    template_name = 'webapp/payment/form.html'
    success_url = reverse_lazy('webapp:payment-list')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['customer', 'ticket', 'gift_certificate', 'status', 'operation_type']
    template_name = 'webapp/payment/form.html'
    success_url = reverse_lazy('webapp:payment-list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'webapp/payment/confirm_delete.html'
    success_url = reverse_lazy('webapp:payment-list')
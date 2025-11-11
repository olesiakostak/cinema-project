from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.catalog.repositories import unit_of_work
from django.urls import reverse_lazy
from app.catalog.models import GiftCertificate
from ..forms import GiftCertificateForm

class GiftCertificateListView(ListView):
    template_name = 'webapp/gift_certificate/list.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        return unit_of_work.gift_certificates.get_all()

class GiftCertificateDetailView(DetailView):
    template_name = 'webapp/gift_certificate/detail.html'
    context_object_name = 'certificate'

    def get_queryset(self):
        return unit_of_work.gift_certificates.get_all()
    
class GiftCertificateCreateView(CreateView):
    model = GiftCertificate
    form_class = GiftCertificateForm
    template_name = 'webapp/gift_certificate/form.html'
    success_url = reverse_lazy('webapp:gift-certificate-list')

class GiftCertificateUpdateView(UpdateView):
    model = GiftCertificate
    form_class = GiftCertificateForm
    template_name = 'webapp/gift_certificate/form.html'
    success_url = reverse_lazy('webapp:gift-certificate-list')

class GiftCertificateDeleteView(DeleteView):
    model = GiftCertificate
    template_name = 'webapp/gift_certificate/confirm_delete.html'
    success_url = reverse_lazy('webapp:gift-certificate-list')
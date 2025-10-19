from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FilmSerializer, GenreSerializer, HallSerializer, CustomerSerializer, GiftCertificateSerializer, SeatSerializer, SessionSerializer, TicketSerializer, PaymentSerializer
from .repositories import unit_of_work

class BaseRepositoryViewSet(viewsets.ModelViewSet):
    repository = None

    def get_queryset(self):
        return self.repository.get_all()
    
    def perform_create(self, serializer):
        return self.repository.create(**serializer.validated_data)

class FilmViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.films
    serializer_class = FilmSerializer

class GenreViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.genres
    serializer_class = GenreSerializer

class HallViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.halls
    serializer_class = HallSerializer

class CustomerViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.customers
    serializer_class = CustomerSerializer

class GiftCertificateViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.gift_certificates
    serializer_class = GiftCertificateSerializer

class SeatViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.seats
    serializer_class = SeatSerializer

class SessionViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.sessions
    serializer_class = SessionSerializer

class TicketViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.tickets
    serializer_class = TicketSerializer

class PaymentViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.payments
    serializer_class = PaymentSerializer
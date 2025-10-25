from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FilmSerializer, GenreSerializer, HallSerializer, CustomerSerializer, GiftCertificateSerializer, SeatSerializer, SessionSerializer, TicketSerializer, PaymentSerializer
from .repositories import unit_of_work
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Sum

class BaseRepositoryViewSet(viewsets.ModelViewSet):
    repository = None

    def get_queryset(self):
        return self.repository.get_all()
    
    def perform_create(self, serializer):
        serializer.instance = self.repository.create(**serializer.validated_data)
    
    def perform_update(self, serializer):
        self.repository.update(obj_id=serializer.instance.id, **serializer.validated_data)
    
    def perform_destroy(self, instance):
        self.repository.delete(instance.id)

class FilmViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.films
    serializer_class = FilmSerializer

    @action(detail=False, methods=['get']) 
    def performance_report(self, request):
        data = unit_of_work.films.get_all().annotate(
            total_sessions=Count('session', distinct=True),
            number_of_sold_tickets=Count('session__ticket'),
            total_revenue=Sum('session__ticket__base_price')
            ).values(
                'title',
                'rating',
                'total_sessions',
                'number_of_sold_tickets',
                'total_revenue'
            )
        return Response(list(data))

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
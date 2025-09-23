from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FilmSerializer, GenreSerializer, HallSerializer, CustomerSerializer, GiftCertificateSerializer, SeatSerializer, SessionSerializer, TicketSerializer, PaymentSerializer
from .repositories import unit_of_work
from rest_framework.decorators import action
from rest_framework.response import Response

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
        data = self.repository.get_performance_stats()
        return Response(list(data))

class GenreViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.genres
    serializer_class = GenreSerializer

    @action(detail=False, methods=['get'])
    def genre_popularity(self, request):
        data = self.repository.get_genres_popularity()
        return Response(list(data))

class HallViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.halls
    serializer_class = HallSerializer

    @action(detail=False, methods=['get'])
    def performance_report(self, request):
        data = self.repository.get_hall_stats()
        return Response(list(data))

class CustomerViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.customers
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['get'])
    def customer_report(self, request):
        data = self.repository.get_top_customers()
        return Response(list(data))

class GiftCertificateViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.gift_certificates
    serializer_class = GiftCertificateSerializer

    @action(detail=False, methods=['get'])
    def usage_report(self, request):
        data = self.repository.get_usage_stats()
        return Response(list(data))

class SeatViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.seats
    serializer_class = SeatSerializer

class SessionViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.sessions
    serializer_class = SessionSerializer

    @action(detail=False, methods=['get'])
    def time_report(self, request):
        data = self.repository.get_session_time_stats()
        return Response(list(data))

class TicketViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.tickets
    serializer_class = TicketSerializer

    @action(detail=False, methods=['get'])
    def booked_tickets(self, request):
        tickets = self.repository.get_booked_tickets()
        serializer = self.get_serializer(tickets, many=True)
        return Response(serializer.data)

class PaymentViewSet(BaseRepositoryViewSet):
    repository = unit_of_work.payments
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['get'])
    def successful_payments(self, request):
        payments = self.repository.get_successful_payments()
        serializer = self.get_serializer(payments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fail_payments(self, request):
        payments = self.repository.get_fail_payments()
        serializer = self.get_serializer(payments, many=True)
        return Response(serializer.data)
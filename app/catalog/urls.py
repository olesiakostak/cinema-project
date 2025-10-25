from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet, GenreViewSet, HallViewSet, CustomerViewSet, GiftCertificateViewSet, SeatViewSet, SessionViewSet, TicketViewSet, PaymentViewSet

router = DefaultRouter()

router.register(r'films', FilmViewSet, basename='film')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'halls', HallViewSet, basename='hall')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'gift-certificates', GiftCertificateViewSet, basename='gift-certificate')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [path('', include(router.urls))]


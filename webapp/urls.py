from django.urls import path
from django.views.generic import TemplateView
from . import views
from . import dashboard

app_name = 'webapp'


urlpatterns = [
    path('', TemplateView.as_view(template_name='webapp/home.html'), name='home-page'),

    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genres/add/', views.GenreCreateView.as_view(), name='genre-add'),
    path('genres/update/<int:pk>/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genres/delete/<int:pk>/', views.GenreDeleteView.as_view(), name='genre-delete'),
    path('genres/dashboard/', dashboard.genres_analytics, name='genre-analytics'),

    path('films/', views.FilmListView.as_view(), name='film-list'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film-detail'),
    path('films/add/', views.FilmCreateView.as_view(), name='film-add'),
    path('films/update/<int:pk>/', views.FilmUpdateView.as_view(), name='film-update'),
    path('films/delete/<int:pk>/', views.FilmDeleteView.as_view(), name='film-delete'),
    path('films/dashboard/', dashboard.films_analytics, name='film-analytics'),

    path('halls/', views.HallListView.as_view(), name='hall-list'),
    path('halls/<int:pk>/', views.HallDetailView.as_view(), name='hall-detail'),
    path('halls/add/', views.HallCreateView.as_view(), name='hall-add'),
    path('halls/update/<int:pk>/', views.HallUpdateView.as_view(), name='hall-update'),
    path('halls/delete/<int:pk>/', views.HallDeleteView.as_view(), name='hall-delete'),
    path('halls/dashboard/', dashboard.halls_analytics, name='hall-analytics'),

    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    path('customers/update/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    path('customers/dashboard/', dashboard.customers_analytics, name='customer-analytics'),


    path('gift-certificates/', views.GiftCertificateListView.as_view(), name='gift-certificate-list'),
    path('gift-certificates/<int:pk>/', views.GiftCertificateDetailView.as_view(), name='gift-certificate-detail'),
    path('gift-certificates/add/', views.GiftCertificateCreateView.as_view(), name='gift-certificate-add'),
    path('gift-certificates/update/<int:pk>/', views.GiftCertificateUpdateView.as_view(), name='gift-certificate-update'),
    path('gift-certificates/delete/<int:pk>/', views.GiftCertificateDeleteView.as_view(), name='gift-certificate-delete'),
    path('gift-certificates/dashboard/', dashboard.gift_certificates_analytics, name='gift-certificate-analytics'),

    path('seats/', views.SeatListView.as_view(), name='seat-list'),
    path('seats/<int:pk>/', views.SeatDetailView.as_view(), name='seat-detail'),
    path('seats/add/', views.SeatCreateView.as_view(), name='seat-add'),
    path('seats/update/<int:pk>/', views.SeatUpdateView.as_view(), name='seat-update'),
    path('seats/delete/<int:pk>/', views.SeatDeleteView.as_view(), name='seat-delete'),

    path('sessions/', views.SessionListView.as_view(), name='session-list'),
    path('sessions/<int:pk>/', views.SessionDetailView.as_view(), name='session-detail'),
    path('sessions/add/', views.SessionCreateView.as_view(), name='session-add'),
    path('sessions/update/<int:pk>/', views.SessionUpdateView.as_view(), name='session-update'),
    path('sessions/delete/<int:pk>/', views.SessionDeleteView.as_view(), name='session-delete'),
    path('sessions/dashboard/', dashboard.sessions_analytics, name='session-analytics'),

    path('tickets/', views.TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/add/', views.TicketCreateView.as_view(), name='ticket-add'),
    path('tickets/update/<int:pk>/', views.TicketUpdateView.as_view(), name='ticket-update'),
    path('tickets/delete/<int:pk>/', views.TicketDeleteView.as_view(), name='ticket-delete'),

    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/add/', views.PaymentCreateView.as_view(), name='payment-add'),
    path('payments/update/<int:pk>/', views.PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/delete/<int:pk>/', views.PaymentDeleteView.as_view(), name='payment-delete'),

    path('external/airports/', views.ExternalAirportListView.as_view(), name='external-airport-list'),
    path('analytics/benchmark/', views.analytics_dashboard, name='benchmark')

]
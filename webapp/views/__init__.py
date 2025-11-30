from .genre import GenreListView, GenreDetailView, GenreCreateView, GenreUpdateView, GenreDeleteView
from .film import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView
from .hall import HallListView, HallDetailView, HallCreateView, HallUpdateView, HallDeleteView
from .customer import CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from .gift_certificate import GiftCertificateListView, GiftCertificateDetailView, GiftCertificateCreateView, GiftCertificateUpdateView, GiftCertificateDeleteView
from .seat import SeatListView, SeatDetailView, SeatCreateView, SeatUpdateView, SeatDeleteView
from .session import SessionListView, SessionDetailView, SessionCreateView, SessionUpdateView, SessionDeleteView
from .ticket import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView
from .payment import PaymentListView, PaymentDetailView, PaymentCreateView, PaymentDeleteView, PaymentUpdateView
from .external_api import ExternalAirportListView
from ..dashboard.analytics import analytics_dashboard
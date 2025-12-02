from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    duration = models.SmallIntegerField()
    rating  = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.DateField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, through='FilmGenre')

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title
    
class FilmGenre(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, db_column='film_id')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='genre_id')

    class Meta:
        db_table = 'film_genre'
        unique_together = ('film', 'genre')

    def __str__(self):
        return f'Film: {self.film}, Genre: {self.genre}'


class Hall(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class ScreenType(models.TextChoices):
        TWO_D = '2D', '2D'
        THREE_D = '3D', '3D'
        IMAX = 'IMAX', 'IMAX'
        FOUR_D = '4DX', '4DX'

    screen_type = models.CharField(max_length=5, choices=ScreenType.choices)

    class Meta:
        db_table = 'hall'
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class GiftCertificate(models.Model):
    code = models.CharField(max_length=64, unique=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
    expiration_date = models.DateField()

    class Meta:
        db_table = 'gift_certificate'

    def __str__(self):
        return self.code

class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, db_column='hall_id')
    row = models.IntegerField(db_column='row_num')
    seat = models.IntegerField(db_column='seat_num')
    
    class Meta:
        unique_together = ('hall', 'row', 'seat')
        db_table = 'seat'

    def __str__(self):
        return f'Seat: hall - {self.hall}, row - {self.row}, seat - {self.seat}'


class Session(models.Model):
    film = models.ForeignKey(Film, db_column='film_id', on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, db_column='hall_id', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Status(models.TextChoices):
        SCHEDULED = 'scheduled', 'Scheduled'
        CANCELED = 'canceled', 'Canceled'
        FINISHED = 'finished', 'Finished'

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.SCHEDULED)

    class Meta:
        db_table = 'session'

    def __str__(self):
        return f'Session: film - {self.film}, hall - {self.hall}'

class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING, db_column='session_id')
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING, db_column='seat_id')
    base_price = models.DecimalField(max_digits=9, decimal_places=2)

    class Status(models.TextChoices):
        BOOKED = 'booked', 'Booked'
        SOLD = 'sold', 'Sold'
        CANCELED = 'canceled', 'Canceled'
        REFUNDED = 'refunded', 'Refunded'

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.BOOKED)
    purchase_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'seat')
        db_table = 'ticket'

    def __str__(self):
        return f'Ticket: session - {self.session}, seat - {self.seat}'

class Payment(models.Model):
    customer = models.ForeignKey(Customer, db_column='customer_id', on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, db_column='ticket_id', on_delete=models.DO_NOTHING)
    gift_certificate = models.ForeignKey(GiftCertificate, db_column='gift_certificate_id', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Status(models.TextChoices):
        SUCCESS = 'success', 'Success',
        FAIL = 'fail', 'Fail',
        PENDING = 'pending', 'Pending'

    class OperationType(models.TextChoices):
        SALE = 'sale', 'Sale'
        REFUND = 'refund', 'Refund'
        GIFT_REDEEM = 'gift_redeem', 'Gift Redeem'
    
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    operation_type = models.CharField(max_length=15, choices=OperationType.choices, default=OperationType.SALE)
    processed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f'Payment: customer_id - {self.customer}, ticket - {self.ticket}'


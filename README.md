# Cinema Project

Web application for cinema management on Django: REST API + administrative web panel with analytical dashboards. The project utilized architectural patterns (Repository, Unit of Work) and generated data-oriented reports.

## Functionality

**REST API (Django REST Framework)**
- CRUD for core entities: movies, genres, halls, venues, screenings, customers, tickets, payments, gift certificates
- Analytical endpoints on top of business logic: `performance_report` (movie revenue), `genre_popularity, `customer_report` (top clients), `usage_report` (use of certificates), `time_report` (session statistics), `successful_payments` /`fail_payments`
- Basic Authentication (HTTP Basic Auth)

**Productivity**
- Benchmarking module that compares the amountThreadPoolExecutor` vs the amountProcessPoolExecutor` in parallel requests to the database under different loads, with visualization of the results (`/analytics/benchmark/`)

## Tech Stack

`Python` · `Django 5` · `Django REST Framework` · `MySQL` · `pandas` · `Plotly` · `Bokeh` · `requests`

## Architecture

The business logic of the API is placed in a separate layer of repositories according to the **Repository + Unit of Work** pattern (`app/catalog/repositories/`), which separates access to data from view logic and facilitates testing and reuse of requests (including complex aggregations for reports).

```
cinema-project/
├── cinema_project/       # Django-configuration of the project (settings, urls, wsgi/asgi)
├── app/catalog/          # REST API: models, serializers, view sets, repositories
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── repositories/     # Repository + Unit of Work
├── webapp/                # Admin Webbar
│   ├── views/             # CRUD-views by entity + booking
│   ├── dashboard/         # Analytical dashboards (pandas + Plotly + Bokeh)
│   ├── bechmarks.py        # Benchmark Thread vs Process
│   └── templates/
├── manage.py
└── requirements.txt
```

## Models

`Film` · `Genre` · `Hall` · `Seat` · `Session` · `Customer` · `Ticket` · `Payment` · `GiftCertificate` — with status logic (booking/sale/cancellation/return of ticket, payment status and transactions).


## Launch with Docker

Docker Compose starts the Django application and a MySQL database. From the project root, run:

```bash
docker compose up --build
```

The application is available at `http://127.0.0.1:8000/`. Create an administrator in another terminal with:

```bash
docker compose exec web python manage.py createsuperuser
```

Stop the services with `docker compose down`. Add `-v` when stopping if you also want to remove the database volume.


## Launch locally

1. Clone repository and set dependencies:
   ```bash
   git clone https://github.com/olesiakostak/cinema-project.git
   cd cinema-project
   pip install -r requirements.txt
   ```
2. Create a MySQL database and configure its connection with the `MYSQL_*` environment variables used by `cinema_project/settings.py`.
3. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run the server
   ```bash
   python manage.py runserver
   ```
5. Open `http://127.0.0.1:8000/` — web panel, `http://127.0.0.1:8000/api/` — REST API, `http://127.0.0.1:8000/admin/` — Django admin.


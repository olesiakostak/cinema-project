from .analytics import fetch_data, filter_df_data, calculate_stats, build_chart
from django.shortcuts import render


def films_analytics(request):

    min_revenue = request.GET.get('min_revenue')
    max_revenue = request.GET.get('max_revenue')

    df_films = fetch_data("api/films/performance_report/")

    if df_films is not None and not df_films.empty:
        df_films = filter_df_data(df_films, "total_revenue", x_min=min_revenue, x_max=max_revenue)
        stats_films = calculate_stats(df_films, "total_revenue", group_by_col="rating")
        html_films = build_chart(df_films, "title", "total_revenue", "Film revenue", "bar")
    else:
        stats_films = {}
        html_films = "<p>Missing data</p>"

  

    # # ---------------------------------------------------------
    # # 4. СЕАНСИ (Sessions Time)
    # # ---------------------------------------------------------
    # df_sessions = fetch_data("api/sessions/time_report/")
    # stats_sessions = calculate_stats(df_sessions, "num_of_sessions")
    # html_sessions = build_chart(df_sessions, "hour", "num_of_sessions", "Time report", "line")

    # # ---------------------------------------------------------
    # # 5. КЛІЄНТИ (Top Customers) - можна теж додати фільтр!
    # # ---------------------------------------------------------
    # min_spend = request.GET.get('min_spend') # Додатковий фільтр
    
    # df_customers = fetch_data("api/customers/customer_report/")
    
    # if df_customers is not None and not df_customers.empty:
    #     df_customers = filter_df_data(df_customers, "total_spend", x_min=min_spend)
    #     stats_customers = calculate_stats(df_customers, "total_spend")
    #     # Використовуємо 'last_name' або 'first_name' для осі X
    #     html_customers = build_chart(df_customers, "last_name", "total_spend", "Top clients", "bar")
    # else:
    #     stats_customers = {}
    #     html_customers = "<p>Немає даних</p>"

    # # ---------------------------------------------------------
    # # 6. СЕРТИФІКАТИ (Gift Certificates)
    # # ---------------------------------------------------------
    # df_certs = fetch_data("api/gift-certificates/usage_report/")
    # stats_certs = calculate_stats(df_certs, "usage_count")
    # html_certs = build_chart(df_certs, "code", "usage_count", "Gift-Certificates Usage", "bar")

    # # ---------------------------------------------------------
    # # Рендеринг шаблону
    # # ---------------------------------------------------------
    return render(request, "webapp/film/dashboard.html", {
        "chart_films": html_films,
        "stats_films": stats_films,
        "min_revenue_val": min_revenue, 
        "max_revenue_val": max_revenue

        # # Жанри
        # "chart_genres": html_genres,
        # "stats_genres": stats_genres,

        # # Зали
        # "chart_halls": html_halls,
        # "stats_halls": stats_halls,

        # # Сеанси
        # "chart_sessions": html_sessions,
        # "stats_sessions": stats_sessions,

        # # Клієнти
        # "chart_customers": html_customers,
        # "stats_customers": stats_customers,
        # "min_spend_val": min_spend,

        # # Сертифікати
        # "chart_gift_certificates": html_certs,
        # "stats_gift_certificates": stats_certs
    })
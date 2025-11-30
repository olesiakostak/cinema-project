from .analytics import fetch_data, filter_df_data, calculate_stats, build_chart
from django.shortcuts import render


def genres_analytics(request):

    df_genres = fetch_data("api/genres/genre_popularity/")

    if df_genres is not None and not df_genres.empty:
        stats_genres = calculate_stats(df_genres, "films_count")
        html_genres = build_chart(df_genres, "name", "films_count", "Genre popularity", "pie")
    else:
        stats_genres = {}
        stats_genres = "<p>Дані відсутні</p>"


    return render(request, "webapp/genre/dashboard.html", {
        "chart_genres": html_genres,
        "stats_genres": stats_genres,
    })
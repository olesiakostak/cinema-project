from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def genres_analytics(request):

    df_genres = fetch_data("api/genres/genre_popularity/")

    if df_genres is not None and not df_genres.empty:
        stats_genres = calculate_stats(df_genres, "films_count")

        html_genres = build_plotly_chart(
            df=df_genres, 
            x_param="name", 
            y_param="films_count", 
            title="Genre popularity", 
            chart_type="pie")
        
        bokeh_script, bokeh_div = build_bokeh_chart(
            df=df_genres,
            x_param="name",
            y_param="films_count",
            title="Genre popularity",
            chart_type="bar"
        )
    else:
        stats_genres = {}
        html_genres = "<p>Missing data</p>"
        bokeh_script=""
        bokeh_div=""


    return render(request, "webapp/genre/dashboard.html", {
        "chart_genres": html_genres,
        "stats_genres": stats_genres,

        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,
    })
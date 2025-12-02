from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def genres_analytics(request):

    df_genres = fetch_data("api/genres/genre_popularity/")
    chart_type = request.GET.get('chart_type', 'bar')


    if df_genres is not None and not df_genres.empty:
        stats_genres = calculate_stats(df_genres, "films_count")

        html_genres = build_plotly_chart(
            df=df_genres, 
            x_param="name", 
            y_param="films_count", 
            title="Genre popularity", 
            chart_type=chart_type,
            x_title="Name",
            y_title="Films Count")
        
        bokeh_script, bokeh_div = build_bokeh_chart(
            df=df_genres,
            x_param="name",
            y_param="films_count",
            title="Genre popularity",
            chart_type="bar",
            x_label="Name",
            y_label="Films Count")
    else:
        stats_genres = {}
        html_genres = "<p>Missing data</p>"
        bokeh_script=""
        bokeh_div=""


    return render(request, "webapp/genre/dashboard.html", {
        "chart_genres": html_genres,
        "stats_genres": stats_genres,
        "chart_type": chart_type,

        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,
    })
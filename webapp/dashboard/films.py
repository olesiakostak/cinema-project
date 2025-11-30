from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def films_analytics(request):

    min_revenue = request.GET.get('min_revenue')
    max_revenue = request.GET.get('max_revenue')

    df_films = fetch_data("api/films/performance_report/")

    if df_films is not None and not df_films.empty:
        df_films_filtered = filter_df_data(df_films, "total_revenue", x_min=min_revenue, x_max=max_revenue)
        stats_films = calculate_stats(df_films, "total_revenue", group_by_col="rating")

        html_films = build_plotly_chart(
            df_films_filtered, 
            "title", 
            "total_revenue", 
            "Film revenue", 
            "bar", 
            "Revenue per film", 
            "Film title")

        bokeh_script, bokeh_div = build_bokeh_chart(
                df_films, 
                x_param="title", 
                y_param="number_of_sold_tickets", 
                title="Sold Tickets")
    else:
        stats_films = {}
        html_films = "<p>Missing data</p>"
        bokeh_script = ""  
        bokeh_div = ""

    return render(request, "webapp/film/dashboard.html", {
        "min_revenue_val": min_revenue, 
        "max_revenue_val": max_revenue,
        
        "chart_films": html_films,
        "stats_films": stats_films,

        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,
    })
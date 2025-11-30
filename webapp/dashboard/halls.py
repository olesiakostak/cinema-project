from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart
from django.shortcuts import render


def halls_analytics(request):

    df_halls = fetch_data("api/halls/performance_report/")

    if df_halls is not None and not df_halls.empty:
        stats_halls = calculate_stats(df_halls, "sessions_count") 
        html_halls = build_plotly_chart(df_halls, "name", "sessions_count", "Hall popularity", "pie")
    else:
        stats_halls = {}
        html_halls = "<p>Missing data</p>"


    return render(request, "webapp/hall/dashboard.html", {
        "chart_halls": html_halls,
        "stats_halls": stats_halls,
    })
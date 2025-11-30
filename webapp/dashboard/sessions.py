from .analytics import fetch_data, filter_df_data, calculate_stats, build_chart
from django.shortcuts import render


def sessions_analytics(request):

    df_sessions = fetch_data("api/sessions/time_report/")

    if df_sessions is not None and not df_sessions.empty:
        stats_sessions = calculate_stats(df_sessions, "num_of_sessions")
        html_sessions = build_chart(df_sessions, "hour", "num_of_sessions", "Time report", "line")
    else:
        stats_sessions = {}
        html_sessions = "<p>Missing data</p>"


    return render(request, "webapp/session/dashboard.html", {
        "chart_sessions": html_sessions,
        "stats_sessions": stats_sessions,
    })


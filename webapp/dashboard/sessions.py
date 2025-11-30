from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def sessions_analytics(request):

    df_sessions = fetch_data("api/sessions/time_report/")

    if df_sessions is not None and not df_sessions.empty:
        stats_sessions = calculate_stats(df_sessions, "num_of_sessions")

        html_sessions = build_plotly_chart(
            df=df_sessions, 
            x_param="hour", 
            y_param="num_of_sessions", 
            title="Time report", 
            chart_type="line",
            x_title="Hour",
            y_title="Number of sessions"
            )
        
        bokeh_script, bokeh_div = build_bokeh_chart(
            df_sessions, 
            x_param="hour", 
            y_param="num_of_sessions", 
            title="Time report",
            chart_type="line",
            x_label="Hour",
            y_label="Number of sessions",
            )
    else:
        stats_sessions = {}
        html_sessions = "<p>Missing data</p>"
        bokeh_script = "" 
        bokeh_div = "" 

    return render(request, "webapp/session/dashboard.html", {
        "chart_sessions": html_sessions,
        "stats_sessions": stats_sessions,

        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,
    })


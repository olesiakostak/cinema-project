from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def halls_analytics(request):

    df_halls = fetch_data("api/halls/performance_report/")
    chart_type = request.GET.get('chart_type', 'pie')

    if df_halls is not None and not df_halls.empty:
        stats_halls = calculate_stats(df_halls, "sessions_count") 

        html_halls = build_plotly_chart(
            df=df_halls, 
            x_param="name", 
            y_param="sessions_count", 
            title="Hall popularity", 
            chart_type=chart_type,
            x_title="Hall Name",
            y_title="Number of Sessions")
        
        bokeh_script, bokeh_div = build_bokeh_chart(
            df=df_halls,
            x_param="name",
            y_param="sessions_count",
            title="Hall popularity",
            chart_type="bar",
            x_label="Hall Name",
            y_label="Number of Sessions"
        )
    else:
        stats_halls = {}
        html_halls = "<p>Missing data</p>"
        bokeh_script, bokeh_div 


    return render(request, "webapp/hall/dashboard.html", {
        "chart_halls": html_halls,
        "stats_halls": stats_halls,
        "chart_type": chart_type,

        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,
    })
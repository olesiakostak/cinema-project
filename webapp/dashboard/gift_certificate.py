from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def gift_certificates_analytics(request):

    df_certs = fetch_data("api/gift-certificates/usage_report/")

    if df_certs is not None and not df_certs.empty:
        stats_certs = calculate_stats(df_certs, "usage_count")

        html_certs = build_plotly_chart(
            df=df_certs, 
            x_param="code", 
            y_param="usage_count", 
            title="Gift-Certificates Usage", 
            chart_type="pie")
        bokeh_script, bokeh_div = build_bokeh_chart(
            df=df_certs,
            x_param="code",
            y_param="usage_count",
            title="Gift-Certificates Usage",
            chart_type="bar"
        )
    else:
        stats_certs = {}
        html_certs = "<p>Missing data</p>"
        bokeh_script=""
        bokeh_div=""


    return render(request, "webapp/gift_certificate/dashboard.html", {
        "stats_certs": stats_certs,
        "html_certs": html_certs,
        
        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,
    })
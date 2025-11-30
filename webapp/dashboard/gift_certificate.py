from .analytics import fetch_data, filter_df_data, calculate_stats, build_chart
from django.shortcuts import render


def gift_certificates_analytics(request):

    df_certs = fetch_data("api/gift-certificates/usage_report/")

    if df_certs is not None and not df_certs.empty:
        stats_certs = calculate_stats(df_certs, "usage_count")
        html_certs = build_chart(df_certs, "code", "usage_count", "Gift-Certificates Usage", "bar")
    else:
        stats_certs = {}
        html_certs = "<p>Missing data</p>"


    return render(request, "webapp/gift_certificate/dashboard.html", {
        "stats_certs": stats_certs,
        "html_certs": html_certs,
    })
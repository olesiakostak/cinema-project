from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart
from django.shortcuts import render


def customers_analytics(request):

    min_spend = request.GET.get('min_spend') 
    max_spend = request.GET.get('max_spend')
    
    df_customers = fetch_data("api/customers/customer_report/")

    if df_customers is not None and not df_customers.empty:
        df_customers = filter_df_data(df_customers, "total_spend", x_min=min_spend, x_max=max_spend)
        stats_customers = calculate_stats(df_customers, "total_spend")
        html_customers = build_plotly_chart(df_customers, "last_name", "total_spend", "Top clients", "bar")
    else:
        stats_customers = {}
        html_customers = "<p>Missing data</p>"

    return render(request, "webapp/customer/dashboard.html", {
        "html_customers": html_customers,
        "stats_customers": stats_customers,
    })


 
  

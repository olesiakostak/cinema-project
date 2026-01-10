from .analytics import fetch_data, filter_df_data, calculate_stats, build_plotly_chart, build_bokeh_chart
from django.shortcuts import render


def customers_analytics(request):

    min_spend = request.GET.get('min_spend') 
    max_spend = request.GET.get('max_spend')
    chart_type = request.GET.get('chart_type', 'bar')
    
    df_customers = fetch_data("api/customers/customer_report/")

    if df_customers is not None and not df_customers.empty:
        df_customers = filter_df_data(df_customers, "total_spend", x_min=min_spend, x_max=max_spend)
        stats_customers = calculate_stats(df_customers, "total_spend")
        
        html_customers = build_plotly_chart(
            df=df_customers, 
            x_param="last_name", 
            y_param="total_spend", 
            title="Top clients", 
            chart_type=chart_type,
            x_title="Last Name",
            y_title="Total Spend")
        
        bokeh_script, bokeh_div = build_bokeh_chart(
            df=df_customers,
            x_param="last_name",
            y_param="purchases_num",
            title="Top clients",
            chart_type="bar",
            x_label="Last Name",
            y_label="Number of purchases")
    else:
        stats_customers = {}
        html_customers = "<p>Missing data</p>"
        bokeh_script="" 
        bokeh_div=""

    return render(request, "webapp/customer/dashboard.html", {
        "html_customers": html_customers,
        "stats_customers": stats_customers,
        "chart_type": chart_type,

        "bokeh_script": bokeh_script,
        "bokeh_div": bokeh_div,        
    })


 
  

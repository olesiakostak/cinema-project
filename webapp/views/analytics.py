from ..bechmarks import get_benchmark_chart
from django.shortcuts import render

def analytics_dashboard(request):
    chart_benchmark_workers, chart_benchmark_requests = get_benchmark_chart()

    return render(request, "webapp/analytics.html", {
        "chart_benchmark_workers": chart_benchmark_workers,  
        "chart_benchmark_requests": chart_benchmark_requests, 
    })
from ..bechmarks import get_benchmark_chart
from django.shortcuts import render

def benchmark_dashboard(request):

    chart_html = get_benchmark_chart()

    return render(request, "webapp/analytics.html", {
        "chart_benchmark": chart_html
    })
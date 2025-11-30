import requests
import pandas as pd
import plotly.express as px
from django.shortcuts import render

auth=(USERNAME, PASSWORD)

def get_chart_from_api(api_url, x_param, y_param, title, group_by_col=None, agg_func="mean", chart_type="bar"):
    response = requests.get(BASE_URL + api_url, auth=auth)

    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        
        if not df.empty:
            stats = {"mean": df[y_param].mean(), 
                     "min": df[y_param].min(), 
                     "max": df[y_param].max(), 
                     "median": df[y_param].median()}
            
            if (group_by_col) and (group_by_col in df.columns):
                stats['grouped_analysis'] = df.groupby(group_by_col)[y_param].agg(agg_func).to_dict()

            if chart_type == "line":
                fig = px.line(df, x=x_param, y=y_param, title=title)
            elif chart_type == "pie": 
                fig = px.pie(df, names=x_param, values=y_param, title=title)
            else:
                fig = px.bar(df, x=x_param, y=y_param, title=title)

            char_field = fig.to_html(full_html=False)
            return char_field, stats
        else:
            return f"Data Frame is empty", {}
    else:
        return f"<p>API error: {response.status_code}<p>", {}


def analytics_dashboard(request):
    
    html_films, stats_films = get_chart_from_api(
        api_url="api/films/performance_report/",
        x_param="title",
        y_param="total_revenue",
        title="Film revenue",
        chart_type="bar"
    )

    html_genres, stats_genres = get_chart_from_api(
        api_url="api/genres/genre_popularity/",
        x_param="name", 
        y_param="films_count",
        title="Genre popularity",
        chart_type="pie"
    )

    html_halls, stats_halls = get_chart_from_api(
        api_url="api/halls/performance_report/",
        x_param="name",
        y_param="sessions_count",
        title="Hall popularity",
        chart_type="pie"
    )

    html_sessions, stats_sessions = get_chart_from_api(
        api_url="api/sessions/time_report/",
        x_param="hour",
        y_param="num_of_sessions",
        title="Time report",
        chart_type="line"
    )

    html_customers, stats_customers = get_chart_from_api(
        api_url="api/customers/customer_report/",
        x_param="id",
        y_param="total_spend",
        title="Top clients",
        chart_type="bar"
    )

    html_gift_certificates, stats_gift_certificates = get_chart_from_api(
        api_url="api/gift-certificates/usage_report/",
        x_param="code",
        y_param="usage_count",
        title="Gift-Certificates Popularity",
        chart_type="bar"
    )

    return render(request, "webapp/analytics.html", {
        "chart_films": html_films,
        "stats_films": stats_films,

        "chart_genres": html_genres,
        "stats_genres": stats_genres,

        "chart_halls": html_halls,
        "stats_halls": stats_halls,

        "chart_sessions": html_sessions,
        "stats_sessions": stats_sessions,

        "chart_customers": html_customers,
        "stats_customers": stats_customers,

        "chart_gift_certificates": html_gift_certificates,
        "stats_gift_certificates": stats_gift_certificates
    })

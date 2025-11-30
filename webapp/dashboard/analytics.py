import requests
import pandas as pd
import plotly.express as px

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'olesia'
PASSWORD = 'olesia1488'
auth=(USERNAME, PASSWORD)


def fetch_data(api_url):
    response = requests.get(BASE_URL + api_url, auth=auth)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return None
    

def calculate_stats(df, y_param, group_by_col=None, agg_func="mean"):
    if not df.empty and df is not None:
        stats = {"mean": df[y_param].mean(), 
                 "min": df[y_param].min(), 
                 "max": df[y_param].max(), 
                 "median": df[y_param].median()}
        
        if (group_by_col) and (group_by_col in df.columns):
                stats['grouped_analysis'] = df.groupby(group_by_col)[y_param].agg(agg_func).to_dict()
        
        return stats
    else:
        return {}
    
def filter_df_data(df, y_param, x_min=None, x_max=None):
    if x_min:
        df = df[df[y_param] > float(x_min)]
    if x_max:
        df = df[df[y_param] < float(x_max)]
    
    return df


def build_chart(df, x_param, y_param, title, chart_type="bar"):
    if chart_type == "line":
        fig = px.line(df, x=x_param, y=y_param, title=title)
    elif chart_type == "pie": 
        fig = px.pie(df, names=x_param, values=y_param, title=title)
    else:
        fig = px.bar(df, x=x_param, y=y_param, title=title)

    char_field = fig.to_html(full_html=False)
    return char_field
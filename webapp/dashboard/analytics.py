import requests
import pandas as pd
import plotly.express as px
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral6

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'olesia'
PASSWORD = 'python1111'
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


def build_plotly_chart(df, x_param, y_param, title, chart_type="bar", x_title=None, y_title=None):
    if chart_type == "line":
        fig = px.line(df, x=x_param, y=y_param, title=title)
    elif chart_type == "pie": 
        fig = px.pie(df, names=x_param, values=y_param, title=title)
    else:
        fig = px.bar(df, x=x_param, y=y_param, title=title)

    if x_title:
        fig.update_layout(xaxis_title=x_title)
    if y_title:
        fig.update_layout(yaxis_title=y_title)

    char_field = fig.to_html(full_html=False)
    return char_field


def build_bokeh_chart(df, x_param, y_param, title, chart_type="bar", x_label=None, y_label=None):
    source = ColumnDataSource(df)
    
    if chart_type == "line":
        fig = figure(height=400, 
                     sizing_mode='stretch_width', 
                     title=title)
        
        fig.line(x=x_param, y=y_param, source=source, line_width=3)
        fig.circle(x=x_param, y=y_param, source=source, size=8, fill_color="white", line_width=2)

        fig.x_range.range_padding = 0
    else:
        x_range = df[x_param].astype(str).tolist()

        fig = figure(x_range=x_range, 
                     height=400, 
                     sizing_mode='stretch_width', 
                     title=title)
        
        fig.vbar(x=x_param, top=y_param, width=0.8, source=source, line_color='white')
        fig.xaxis.major_label_orientation = -1.2

    fig.xgrid.grid_line_color = None
    fig.y_range.start = 0

    hover = HoverTool()
    hover.tooltips = [
        (title, f"@{x_param}"),      
        ("Value", f"@{y_param}{{0.00}}") 
    ]
    fig.add_tools(hover)

    if x_label:
        fig.xaxis.axis_label=x_label
    if y_label:
        fig.yaxis.axis_label=y_label
    
    script, div = components(fig)
    return script, div
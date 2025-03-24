import dash
from dash import html

def page_1():
    return html.Div([
        html.H1("Page 1: Visualization 1"),
        html.Div([
            html.P("This is the first page of the app. Here, you could display a plot or other visualization."),
        ])
    ])
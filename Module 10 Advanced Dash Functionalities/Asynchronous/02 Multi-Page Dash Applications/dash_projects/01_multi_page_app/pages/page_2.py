import dash
from dash import html

def page_2():
    return html.Div([
        html.H1("Page 2: Visualization 2"),
        html.Div([
            html.P("This is the second page of the app. Display another visualization or content here."),
        ])
    ])
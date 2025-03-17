import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Dashboard Title", style={"textAlign": "center"}),

    html.Div([
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": "Option 1", "value": "opt1"},
                     {"label": "Option 2", "value": "opt2"}],
            value="opt1"
        )
    ], style={"width": "50%", "margin": "auto"}),

    dcc.Graph(
        id="example-graph",
        figure={
            "data": [{"x": [1, 2, 3], "y": [3, 1, 6], "type": "bar"}],
            "layout": {"title": "Example Graph"}
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
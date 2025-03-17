import dash
from dash import dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout (UI components)
app.layout = html.Div(children=[
    html.H1("Hello, Dash!", style={"textAlign": "center"}),
    html.P("This is a simple Dash app.", style={"textAlign": "center"}),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
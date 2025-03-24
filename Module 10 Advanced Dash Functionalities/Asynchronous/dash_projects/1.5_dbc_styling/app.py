import dash
import dash_bootstrap_components as dbc
from dash import html

# Initialize Dash app 
# TODO: Try changing dbc.themes.FLATLY to other themes like BOOTSTRAP, CYBORG, DARKLY, etc.
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# App Layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Styled Dashboard", className="text-center mt-4"))),

    dbc.Row(dbc.Col(html.P("This dashboard uses a DBC theme.", className="text-center"))),

    # Button Example (Shows theme styling)
    dbc.Row(dbc.Col(dbc.Button("Click Me", color="primary", className="mt-3"), className="text-center")),

    # Alert Example (Demonstrates theme colors)
    dbc.Row(dbc.Col(dbc.Alert("This is an example alert!", color="info", className="mt-3"))),
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

import dash
from dash import html

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    html.H1("Simple Dash App with External Google Font Styling"),
    html.P("This is a simple paragraph using external google font styling.")
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

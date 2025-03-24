import dash
from dash import html

# Using an external Bootstrap stylesheet
external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"]

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# App Layout
app.layout = html.Div([
    html.Div([
        html.H1("Welcome to My Dash App", className="text-primary text-center"),
        html.P("This is a simple example using a hosted Bootstrap stylesheet.", className="text-center"),
    ], className="container mt-5")
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
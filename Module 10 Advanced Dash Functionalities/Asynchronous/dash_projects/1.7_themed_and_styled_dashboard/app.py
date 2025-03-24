import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px

# Initialize Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Create a scatter plot using Plotly Express (iris dataset)
fig = px.scatter(px.data.iris(), x="sepal_width", y="sepal_length", color="species", 
                 title="Iris Dataset: Sepal Width vs Sepal Length")

# Layout with responsive Bootstrap grid
app.layout = dbc.Container([
    html.H1("Styled Dash App", className="text-center text-primary"),  # Title with theme color
    html.P("This app uses external CSS and Bootstrap themes, along with interactive visualizations.", className="text-muted"),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig), width=8),  # Display graph in larger column
        dbc.Col(html.Div("Sidebar Content", className="p-3 bg-light"), width=4)  # Sidebar section
    ])
], fluid=True)  # Make the container fluid for responsive design

if __name__ == "__main__":
    app.run(debug=True)



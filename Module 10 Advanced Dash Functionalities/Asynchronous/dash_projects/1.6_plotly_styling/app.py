import plotly.express as px
import dash
from dash import dcc, html

# Initialize Dash app 
app = dash.Dash(__name__)

# Create a scatter plot using Plotly Express
fig = px.scatter(px.data.iris(), x="sepal_width", y="sepal_length", color="species")

# Update layout styling for the figure
fig.update_layout(
    title="Styled Scatter Plot",
    title_font_size=20,
    font=dict(family="Arial", size=14, color="black"),
    plot_bgcolor="whitesmoke"
)

fig.update_traces(
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    )
)

# App Layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
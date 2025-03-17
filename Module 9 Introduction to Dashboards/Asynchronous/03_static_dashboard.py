import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [100, 200, 150, 300]
})

# Initialize Dash App
app = dash.Dash(__name__)

# Define Layout
app.layout = html.Div(children=[
    html.H1("Static Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(
            id="bar-chart",
            figure=px.bar(df, x="Category", y="Values", title="Bar Chart")
        ),

        dcc.Graph(
            id="pie-chart",
            figure=px.pie(df, names="Category", values="Values", title="Pie Chart")
        )
    ], style={"display": "flex", "justifyContent": "space-around"})
])

if __name__ == "__main__":
    app.run_server(debug=True)
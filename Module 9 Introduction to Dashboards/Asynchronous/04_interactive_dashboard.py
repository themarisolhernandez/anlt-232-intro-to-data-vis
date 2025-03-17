import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Sample Data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Values": [100, 200, 150, 300, 250]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Dashboard", style={"textAlign": "center"}),

    html.Label("Select a category:"),
    dcc.Dropdown(
        id="category-dropdown",
        options=[{"label": cat, "value": cat} for cat in df["Category"]],
        value="A"
    ),

    html.Label("Adjust the bar width:"),
    dcc.Slider(
        id="bar-slider",
        min=0.1,
        max=1.0,
        step=0.1,
        value=0.5
    ),

    dcc.Graph(id="bar-chart")
])

@app.callback(
    Output("bar-chart", "figure"),
    [Input("category-dropdown", "value"),
     Input("bar-slider", "value")]
)
def update_chart(selected_category, bar_width):
    filtered_df = df[df["Category"] == selected_category]
    fig = px.bar(filtered_df, x="Category", y="Values", title=f"Category: {selected_category}")
    fig.update_traces(marker=dict(line=dict(width=bar_width * 10)))
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8081)
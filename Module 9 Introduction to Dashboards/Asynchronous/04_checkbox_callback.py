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
    html.H3("Select categories to display:"),

    dcc.Checklist(
        id="category-checklist",
        options=[{"label": cat, "value": cat} for cat in df["Category"]],
        value=df["Category"].tolist()  # Default: all selected
    ),

    dcc.Graph(id="bar-chart")
])

@app.callback(
    Output("bar-chart", "figure"),
    Input("category-checklist", "value")
)
def update_bar_chart(selected_categories):
    filtered_df = df[df["Category"].isin(selected_categories)]
    fig = px.bar(filtered_df, x="Category", y="Values", title="Filtered Bar Chart")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
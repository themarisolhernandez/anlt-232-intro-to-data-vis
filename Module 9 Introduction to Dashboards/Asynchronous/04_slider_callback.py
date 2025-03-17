import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Sample Data
df = pd.DataFrame({
    "x": list(range(1, 11)),
    "y": [2*i for i in range(1, 11)]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3("Adjust the line thickness:"),
    
    dcc.Slider(
        id="line-slider",
        min=1,
        max=10,
        step=1,
        value=3
    ),
    
    dcc.Graph(id="line-chart")
])

@app.callback(
    Output("line-chart", "figure"),
    Input("line-slider", "value")
)
def update_chart(line_width):
    fig = px.line(df, x="x", y="y", title="Dynamic Line Chart")
    fig.update_traces(line=dict(width=line_width))
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
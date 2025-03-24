import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    dcc.Slider(id="slider", min=0, max=10, value=5),
    html.Div(id="output-1"),
    html.Div(id="output-2"),
    html.Div(id="output-3")
])

# Callback with Multiple Outputs
@app.callback(
    [Output("output-1", "children"),
     Output("output-2", "children"),
     Output("output-3", "children")],
    Input("slider", "value")
)
def update_outputs(value):
    return f"Value: {value}", f"Square: {value**2}", f"Cube: {value**3}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
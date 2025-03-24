import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    html.H1("Simple Dash App with External CSS"),
    
    html.Label("Move the slider:"),
    dcc.Slider(1, 10, step=1, value=5, id="slider"),

    html.P("Selected value: 5", id="output-text")
])

# Callback to update text based on slider
@app.callback(
    Output("output-text", "children"),
    Input("slider", "value")
)
def update_text(value):
    return f"Selected value: {value}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

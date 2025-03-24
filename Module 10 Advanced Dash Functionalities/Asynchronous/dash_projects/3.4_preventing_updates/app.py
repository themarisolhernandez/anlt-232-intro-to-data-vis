import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    dcc.Input(id="num-input", type="number", value=0),
    html.Br(),
    html.Br(),
    html.Div(id="output-message")
])

# Callback with PreventUpdate
@app.callback(
    Output("output-message", "children"),
    Input("num-input", "value")
)
def check_number(value):
    if value < 0:
        raise PreventUpdate  # Prevents updating the output
    return f"Your number is: {value}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
    
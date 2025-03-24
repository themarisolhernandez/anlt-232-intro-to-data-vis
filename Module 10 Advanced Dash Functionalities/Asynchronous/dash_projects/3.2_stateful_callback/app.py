import dash
from dash import dcc, html
from dash.dependencies import State, Input, Output

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    dcc.Input(id="input-text", type="text", value="Dash"),
    html.Button("Submit", id='submit-btn', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Div(id="output-text")
])

# Stateful callback
@app.callback(
    Output("output-text", "children"),
    Input("submit-btn", "n_clicks"),
    State("input-text", "value")
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        return f"You submitted: {value}"
    return "Enter text and click submit."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
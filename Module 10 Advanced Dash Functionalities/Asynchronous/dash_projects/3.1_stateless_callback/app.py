import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    dcc.Input(id="input-text", type="text", value="Dash"),
    html.Br(),
    html.Br(),
    html.Div(id="output-text")
])

# Stateless callback
@app.callback(
    Output("output-text", "children"),
    Input("input-text", "value")
)
def update_output(value):
    return f"You entered: {value}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Layout with dropdown and text output
app.layout = html.Div(children=[
    html.H1("Interactive Dash App", style={"textAlign": "center"}),
    
    dcc.Dropdown(
        id="dropdown",
        options=[
            {"label": "Option 1", "value": "Option 1"},
            {"label": "Option 2", "value": "Option 2"},
            {"label": "Option 3", "value": "Option 3"},
        ],
        value="Option 1",  # Default selection
        clearable=False
    ),

    html.Br(),
    html.P(id="output-text", style={"fontSize": "20px", "textAlign": "center"})
])

# Callback to update text based on dropdown selection
@app.callback(
    Output("output-text", "children"),
    Input("dropdown", "value")
)
def update_output(selected_value):
    return f"You selected: {selected_value}"

if __name__ == "__main__":
    app.run_server(debug=True)
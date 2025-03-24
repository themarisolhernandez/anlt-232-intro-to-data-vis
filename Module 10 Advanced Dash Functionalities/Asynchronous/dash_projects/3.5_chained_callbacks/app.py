import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    dcc.Dropdown(id="dropdown-1", options=[{"label": i, "value": i} for i in ["A", "B", "C"]], value='A'),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id="dropdown-2"),
    html.Br(),
    html.Br(),
    html.Div(id="output")
])

# Chained callbacks
@app.callback(
    Output("dropdown-2", "options"),
    Input("dropdown-1", "value")
)
def update_dropdown(selected_value):
    return [{"label": f"Option {selected_value}-{i}", "value": f"{selected_value}-{i}"} for i in range(1, 4)]

@app.callback(
    Output("output", "children"),
    Input("dropdown-2", "value")
)
def update_output(selected_value):
    return f"You selected: {selected_value}" if selected_value else "Select an option."
    
# Run the app
if __name__ == "__main__":
    app.run(debug=True)

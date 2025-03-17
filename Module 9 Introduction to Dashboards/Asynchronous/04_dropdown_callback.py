import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3("Choose a fruit:"),
    
    dcc.Dropdown(
        id="fruit-dropdown",
        options=[
            {"label": "Apple", "value": "apple"},
            {"label": "Banana", "value": "banana"},
            {"label": "Cherry", "value": "cherry"}
        ],
        value="apple"
    ),
    
    html.Div(id="output-text", style={"margin-top": "20px", "font-size": "20px"})
])

@app.callback(
    Output("output-text", "children"),
    Input("fruit-dropdown", "value")
)
def update_text(selected_fruit):
    return f"You selected: {selected_fruit.capitalize()}"

if __name__ == "__main__":
    app.run_server(debug=True)
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Import pages
from pages.page_1 import page_1
from pages.page_2 import page_2

app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  # Tracks the URL in the browser
    html.Div([
        dcc.Link("Go home", href="/", style={"padding": "10px", "marginRight": "20px"}),  # Added padding and margin
        dcc.Link("Go to Page 1", href="/page-1", style={"padding": "10px", "marginRight": "20px"}),  # Added padding and margin
        dcc.Link("Go to Page 2", href="/page-2", style={"padding": "10px"}),  # Added padding
    ], style={"display": "flex", "flexDirection": "row", "alignItems": "center"}),  # Flexbox for horizontal alignment
    html.Div(id="page-content")  # Where page content will be rendered
])

# Callback to update the page content based on the URL
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/page-1":
        return page_1()  # Calls page_1.py
    elif pathname == "/page-2":
        return page_2()  # Calls page_2.py
    else:
        return html.H1("Welcome to the Multi-Page App!")  # Default page

if __name__ == "__main__":
    app.run(debug=True)
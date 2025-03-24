import dash
from dash import dcc, html

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    html.H1("Simple Heading with Inline Styling", style={"textAlign": "center", "color": "blue"}),
    html.P("This is a paragraph with inline styling.", style={"fontSize": "18px", "color": "#800080"}),
    dcc.Graph(id="example-graph"),

    # Example: Controlling Colors, Fonts, Spacing, and Layout
    # html.Div(
    #         children=[
    #             html.P("One fish. Two fish."),
    #             html.P("Red fish. Blue fish.")
    #         ],
    #          style={
    #              "backgroundColor": "#ECF0F1",
    #              "padding": "10px",
    #              "margin": "20px",
    #              "fontFamily": "Arial"
    #          }
    # ) 
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
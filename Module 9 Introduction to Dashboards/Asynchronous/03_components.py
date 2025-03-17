import dash
from dash import dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout (UI components)
app.layout = html.Div(children=[
    html.H1("Core Components in Dash", style={"textAlign": "center"}),

    # Data Visualization Component
    html.H3("Data Visualization Component", style={"textAlign": "left"}),
    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "line", "name": "Line Chart"},
                {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Bar Chart"}
            ],
            "layout": {"title": "Sample Chart"}
        }
    ),
    html.Br(),  # Line break

    # Selection Menu
    html.H3("Selection Menu", style={"textAlign": "left"}),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {"label": "Option 1", "value": "opt1"},
            {"label": "Option 2", "value": "opt2"},
            {"label": "Option 3", "value": "opt3"}
        ],
        value="opt1",  # Default selection
        clearable=False
    ),
    html.Br(),

    # User Text Input
    html.H3("User Text Input", style={"textAlign": "left"}),
    dcc.Input(
        id="input-text",
        type="text",
        placeholder="Enter text here..."
    ),
    html.Br(),
    html.Br(),

    # Numeric Selection
    html.H3("Numeric Selection", style={"textAlign": "left"}),
    dcc.Slider(
        id="slider",
        min=0,
        max=100,
        step=5,
        value=50
    ),
    html.Br(),

    # Multiple Selections
    html.H3("Multiple Selections", style={"textAlign": "left"}),
    dcc.Checklist(
        id="checklist",
        options=[{"label": "Option A", "value": "A"}, 
                 {"label": "Option B", "value": "B"}],
        value=["A"]  # Default selected value
    )

])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
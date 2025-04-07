from shiny import App, ui, render

# Define the UI for the app
app_ui = ui.page_fluid(
    ui.page_navbar(
        ui.nav_panel("Tab 1", ui.input_slider("num", "Choose a number:", 1, 100, 50)),  # Input tab
        ui.nav_panel("Tab 2", ui.output_text("txt")),  # Output tab
        title="Navbar Example",
    )
)


# Define the server logic
def server(input, output, session):
    # Output the result of the user selection
    @output
    @render.text
    def txt():
        return f"You selected: {input.num()}"

# Create the Shiny app
app = App(app_ui, server)
from shiny import App, ui, render

# Define the UI for the app
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_slider("num", "Choose a number:", 1, 100, 50),  # Input: a slider in the sidebar panel
            title="Sidebar Example",
        ),
        ui.output_text("txt"),  # Output: a text box that will display the result to the main panel
    ),
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







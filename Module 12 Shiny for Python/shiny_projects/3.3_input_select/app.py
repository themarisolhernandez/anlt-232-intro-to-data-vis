from shiny import App, ui, render

# Define the UI
app_ui = ui.page_fluid(
    ui.input_select("category", "Choose a category:", choices=["A", "B", "C"]),
    ui.output_text("selection")
)

# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def selection():
        return f"You selected category: {input.category()}"

# Create the app
app = App(app_ui, server)

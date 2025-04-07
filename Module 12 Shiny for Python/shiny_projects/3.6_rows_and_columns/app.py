from shiny import App, ui, render

# Define the UI for the app
app_ui = ui.page_fluid(
    ui.row(
        ui.column(6, 
            ui.input_slider("num", "Choose a number:", 1, 100, 50),
            ui.output_text("slider_output")
        ),
        ui.column(6, 
            ui.input_select("category", "Choose a category:", choices=["A", "B", "C"]),
            ui.output_text("select_output")
        )
    )
)

# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def slider_output():
        return f"You selected the number: {input.num()}"

    @output
    @render.text
    def select_output():
        return f"You selected the category: {input.category()}"

# Create the Shiny app
app = App(app_ui, server)


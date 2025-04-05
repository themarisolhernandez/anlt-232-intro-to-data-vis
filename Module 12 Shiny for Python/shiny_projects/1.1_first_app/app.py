from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_slider("num", "Choose a number:", 1, 100, 50),  # Input: a slider
    ui.output_text("txt")  # Output: a text box that will display the result
)

def server(input, output, session):
    @output()
    @render.text
    def txt():
        return f"You selected: {input.num()}"

app = App(app_ui, server)
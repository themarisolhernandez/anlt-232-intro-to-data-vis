from shiny import App, ui, render

# Define the UI
app_ui = ui.page_fluid(
    ui.input_text("name", "Enter your name:"),
    ui.output_text("greeting")
)

# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def greeting():
        name = input.name()
        if name:
            return f"Hello, {name}!"
        else:
            return "Please enter your name."

# Create the app
app = App(app_ui, server)

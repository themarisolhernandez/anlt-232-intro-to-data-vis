from shiny import App, ui, render

# Define the UI
app_ui = ui.page_fluid(
    ui.input_checkbox("agree", "I agree to the terms and conditions"),
    ui.output_text("response")
)

# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def response():
        if input.agree():
            return "Thank you for agreeing to the terms and conditions."
        else:
            return "Please agree to the terms and conditions to proceed."

# Create the app
app = App(app_ui, server)

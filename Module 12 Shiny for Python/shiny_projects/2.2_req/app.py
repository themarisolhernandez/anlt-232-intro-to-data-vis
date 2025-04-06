from shiny import App, ui, render, reactive, req

# Define the UI for the app
app_ui = ui.page_fluid(
    ui.h2("Division Calculator"),
    ui.input_numeric("dividend", "Enter a dividend:", value=0),
    ui.input_numeric("divisor", "Enter a divisor (greater than 0):", value=1),
    ui.output_text("division_output")
)

# Define the server logic
def server(input, output, session):
    # Reactive function to validate divisor input
    @reactive.calc
    def validate_input():
        req(input.divisor() > 0)  # Validate the input
        return input.divisor()

    @reactive.calc
    def calc_division():
        return input.dividend() / input.divisor()

    # Output the result of division if divisor input is valid
    @output
    @render.text
    def division_output():
        try:
            validate_input()  # This will throw an error if validation fails
            return f"The result of {input.dividend()} divided by {input.divisor()} is: {calc_division()}"
        except Exception:
            return "Undefined: The divisor must be greater than zero."  # If validation fails, show the error message

# Create the Shiny app
app = App(app_ui, server)

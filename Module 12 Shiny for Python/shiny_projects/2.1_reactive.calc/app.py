from shiny import App, ui, render, reactive

# Define the UI for the app
app_ui = ui.page_fluid(
    ui.h2("Square Calculator"),
    ui.input_numeric("num", "Enter a number:", value=2),
    ui.output_text("square_output")
)

# Define the server logic
def server(input, output, session):
    # NOTE: Using @reactive.calc makes this computation reactive and cacheable.
    @reactive.calc
    def calc_square():
        return input.num() ** 2

    # Output the computation
    @output
    @render.text
    def square_output():
        return f"The square of {input.num()} is {calc_square()}."

        # NOTE: The following also works but calc_square() promotes modularity, and avoids repeating logic.
        # return f"The square of {input.num()} is {input.num() ** 2}."

# Create the Shiny app
app = App(app_ui, server)

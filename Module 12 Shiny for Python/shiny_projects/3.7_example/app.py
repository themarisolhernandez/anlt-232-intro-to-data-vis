import matplotlib.pyplot as plt
import numpy as np
from shiny import App, ui, render

# Define the UI
app_ui = ui.page_fluid(
    ui.row(
        ui.column(4, ui.input_slider("num", "Choose a scaling factor:", 1, 100, 50)),
        ui.column(4, ui.input_select("color", "Choose a color:", choices=["red", "green", "blue", "orange"])),
        ui.column(4, ui.input_checkbox("show_grid", "Show Grid"))
    ),
    ui.output_plot("plot")
)

# Define the server logic
def server(input, output, session):
    @output()
    @render.plot
    def plot():
        x = np.linspace(-10, 10, 100)
        y = np.sin(x) * input.num()

        # Set the color based on the input_select choice
        color = input.color()
        plt.plot(x, y, color=color)

        # Display grid if checkbox is checked
        if input.show_grid():
            plt.grid(True)

        # Set title and labels
        plt.title(f"Plot of Sine Wave with Scaling Factor {input.num()}")
        plt.xlabel("X")
        plt.ylabel("Y")

        # Set fixed axis limits to keep them constant
        plt.xlim(-10, 10)  # Fixed x-axis limits
        plt.ylim(-100, 100)  # Fixed y-axis limits (based on the scaling factor)
        
        return plt.gcf()

# Create the app
app = App(ui=app_ui, server=server)


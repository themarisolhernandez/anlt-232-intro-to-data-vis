import matplotlib.pyplot as plt
import numpy as np
from shiny import App, ui, render

# Define the UI for the app
app_ui = ui.page_fluid(
    ui.h2("Interactive Histogram"),
    ui.input_slider("bins", "Number of bins", min=5, max=50, value=10),
    ui.output_plot("hist_plot")
)

# Define the server logic
def server(input, output, session):
    # Output the histogram using the number of bins specified by the user
    @output
    @render.plot
    def hist_plot():
        np.random.seed(123)
        data = np.random.randn(500)
        plt.hist(data, bins=input.bins())
        plt.title("Histogram of Random Data")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

# Create the Shiny app
app = App(app_ui, server)
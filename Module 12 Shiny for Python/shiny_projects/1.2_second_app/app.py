import matplotlib.pyplot as plt
import numpy as np
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("Interactive Histogram"),
    ui.input_slider("bins", "Number of bins", min=5, max=50, value=10),
    ui.output_plot("hist_plot")
)

def server(input, output, session):
    @output
    @render.plot
    def hist_plot():
        np.random.seed(123)
        data = np.random.randn(500)
        plt.hist(data, bins=input.bins())
        plt.title("Histogram of Random Data")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

app = App(app_ui, server)
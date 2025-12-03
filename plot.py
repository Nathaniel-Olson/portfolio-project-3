# plot.py
# ENDG 233 F25
# Nate Olson, Ruald James
# Pairs L01 -26
# A set of functions which use matplotlib for various plot types

### imports
import numpy as np
import matplotlib.pyplot as plt
from analysis import format_array_to_string

### functions
def comparison_bar_plot(data: np.array, show: bool = True, save: bool = True, filename: str = "comparison_bar_plot.png") -> None:
    """Creates a figure with 2 subplots comparing two countries against some stat.
    Parameters:
        data (np.array): An array with a header row, and two rows of data.
        show (bool): Whether or not to show the graph on the screen
        save (bool): Whether or not to save the graph to the "final_plots" folder.
    """
    header = data[0, 1:].tolist()
    colours = [(0.855, 0.749, 1), (0.565, 0.478, 0.839), (0.310, 0.318, 0.549), (0.173, 0.165, 0.290)]
    types = []

    for title in header:
        types.append(title.split()[0])

    country_1_data = data[1, 1:].astype(float)
    country_2_data = data[2, 1:].astype(float)

    country_1 = data[1, 0]
    country_2 = data[2, 0]

    plt.figure()
    plt.subplot(1,2,1)
    plt.bar(x = types, height = country_1_data, color = colours)
    plt.title(country_1)
    plt.ylabel("Amount per Capita")
    plt.xlabel("Species")
    plt.xticks(ticks = [0,1,2,3], labels = types, rotation = 30)

    plt.subplot(1,2,2)
    plt.bar(x = types, height = country_2_data, color = colours)
    plt.title(country_2)
    plt.xlabel("Species")
    plt.ylabel("Amount per Capita")
    plt.xticks(ticks = [0,1,2,3], labels = types, rotation = 30)

    plt.subplots_adjust(wspace = 0.6, bottom = 0.16)

    if save:
        plt.savefig(f"final_plots/{filename}")
    if show:
        plt.show(block = False)
    return None
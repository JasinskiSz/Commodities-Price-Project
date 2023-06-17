import csv
import os
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from back import back


def create_after_login_window(parentWindow: tk.Tk):
    # Create the main view window
    window = tk.Tk()
    window.title("Stock Market History App")

    width = 1536
    height = 512

    # window size and position
    window.geometry(f"{width}x{height}")

    # Create back button
    tk.Button(window, text="Logout", width=15, height=2,
              command=lambda: back(window, parentWindow)).pack(pady=10)

    # Create a Matplotlib figure and add the donut plot
    fig = create()

    # Create a FigureCanvasTkAgg object to display the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Start the Tkinter event loop
    window.mainloop()


def create():
    commodities_avg_price_dict: dict = get_commodities_avg_price_dict()

    fig = Figure(figsize=(15, 6), dpi=100)
    ax = fig.add_subplot(111)

    for commodity, avg_price in commodities_avg_price_dict.items():
        # Create a bar chart with the average price
        ax.bar(commodity, avg_price, color='blue')

    ax.set_ylabel('Price')
    ax.set_title('30 days Average Price for Commodities')
    ax.set_ylim(0, 10000)  # Adjust the y-axis limits

    return fig


def get_commodities_avg_price_dict():
    commodities_avg_price_dict = {}
    commodities = get_commodities()
    # Read the stock data from a CSV files
    for commodity in commodities:
        commodity_avg_price_dict = {}
        with open(f"data/{commodity}", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            # Read the first 30 rows
            i = 0
            for row in reader:
                if i >= 30:
                    break
                if len(row) == 2 and row[1] != ".":
                    date = row[0]
                    price = float(row[1])
                    commodity_avg_price_dict[date] = price
                    i += 1
        # Calculate the average price and add it to the dictionary
        commodities_avg_price_dict[commodity.split("indicator")[1].split(".")[0]] = sum(
            commodity_avg_price_dict.values()) / len(commodity_avg_price_dict)
    return commodities_avg_price_dict


def get_commodities():
    # Read the commodities from file names in the data folder
    commodities = []
    for filename in os.listdir("data"):
        if filename.startswith("economic_indicator") and filename.endswith(".csv"):
            commodities.append(filename)
    return commodities

"""
In this step we generate charts from our data.
This file has similar code from step2.py
"""

from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [12, 7]
plt.style.use("fivethirtyeight")

# We declare in our list the pairs we need for our figure.
# Each pair is a tuple.
# We split the list into two, to make the plots more readable.

top_pairs = [
    ("MXN", "CHF"),
    ("MXN", "EUR"),
    ("MXN", "GBP"),
    ("MXN", "JPY"),
    ("MXN", "USD")
]

popular_pairs = [
    ("MXN", "ARS"),
    ("MXN", "AUD"),
    ("MXN", "BRL"),
    ("MXN", "CAD"),
    ("MXN", "CNY")
]


def date_converter(value):
    """Converts the UNIX timestamp to a datetime object."""

    return datetime.utcfromtimestamp(float(int(value) / 1000))


def generate_fig(pairs, file_name):
    """
    Converts the .csv into a pandas Dataframe and plots the relevant data.
    In this project, the data was resampled to 1 month intervals.
    """

    for pair in pairs:

        df = pd.read_csv("{}{}.csv".format(pair[0], pair[1]), header=None, names=[
                         "timestamp", "rate", "inversed"], converters={"timestamp": date_converter})
        resampled_df = df.resample("M", on="timestamp").mean().reset_index()

        initial_value = resampled_df["rate"].iloc[0]
        growth_ratios = [(item - initial_value) / initial_value *
                         100 * -1 for item in resampled_df["rate"]]
        
        plt.plot(resampled_df["timestamp"], growth_ratios, label=pair[1])

    plt.ylabel("Percent Change")
    plt.title("Mexican Peso Performance")
    plt.legend()
    plt.draw()
    plt.savefig(file_name)
    plt.close()


if __name__ == "__main__":

    # We call the same function 2 times with different parameters.
    generate_fig(top_pairs, "top5.png")
    generate_fig(popular_pairs, "popular.png")
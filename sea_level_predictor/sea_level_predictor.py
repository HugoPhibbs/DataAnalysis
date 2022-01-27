import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Set up fig and axes
    fig, axes = plt.subplots()
    fig.set_size_inches((10, 10))
    fig.set_dpi(200)

    # Create scatter plot
    axes.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    years = df['Year']
    levels = df['CSIRO Adjusted Sea Level']
    first_lg = linregress(x=years, y=levels)
    x_vals = np.linspace(start= years.min(), stop = 2050, num=171)
    y_vals = first_lg.slope * x_vals + first_lg.intercept
    axes.plot(x_vals, y_vals, color = 'orange')

    # Create second line of best fit
    second_lg = linregress(x=years[years >= 2000], y = levels[years >= 2000])
    x_vals_2 = np.linspace(start = 2000, stop = 2050, num=171)
    y_vals_2 = second_lg.slope*x_vals_2 + second_lg.intercept
    axes.plot(x_vals_2, y_vals_2, color = 'purple')

    # Add labels and title
    axes.set_xlabel('Year')
    axes.set_ylabel("Sea Level (inches)")
    axes.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

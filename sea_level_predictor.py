import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    years_full = range(1880, 2051)
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(years_full, [slope * y + intercept for y in years_full], color='red')

    df_recent = df[df['Year'] >= 2000]
    years_recent = range(2000, 2051)
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    ax.plot(years_recent, [slope2 * y + intercept2 for y in years_recent], color='green')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return ax

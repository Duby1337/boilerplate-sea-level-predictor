import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.drop(['Lower Error Bound', 'Upper Error Bound', 'NOAA Adjusted Sea Level'], axis=1, inplace=True)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(18,10))

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']


    x_extended = range(1880, 2051)

    plt.scatter(x, y)
    plt.xlim(1880, 2050)

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    plt.plot(x_extended, slope * x_extended + intercept, color='red', label="Regression line")

    df_2000 = df[df['Year'] >= 2000]

    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(x_2000, y_2000)

    x_pred_2000 = range(2000, 2051)

    plt.plot(x_pred_2000, slope * x_pred_2000 + intercept, color='purple', label="Regression line")

    plt.title('Rise in Sea Level', fontsize=24)
    plt.xlabel('Year', fontsize=18)
    plt.ylabel('Sea Level (inches)', fontsize=18)
    plt.xticks(range(1850, 2100, 25))







    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
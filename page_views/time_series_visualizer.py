import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from seaborn import FacetGrid

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    filepath_or_buffer='fcc-forum-pageviews.csv',
    parse_dates=[0]
)

df.rename(columns={'  date': 'date'}, inplace=True)
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    axes = df.plot()
    fig = axes.figure

    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)

    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar.reset_index(inplace=True)
    df_bar.drop(columns=['date'], axis=1)

    df_bar = df_bar.groupby(['year', 'month']).mean()
    df_bar.reset_index(inplace=True)
    df_bar.rename(columns={'value': 'views'}, inplace=True)

    facet_grid: FacetGrid = sns.catplot(
        x='year',
        y='views',
        data=df_bar,
        kind='bar',
        hue='month',
        palette='Paired',
        legend = False,
        hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    )

    facet_grid.set_xlabels('Years')
    facet_grid.set_ylabels('Average Page Views')
    facet_grid.ax.legend(title='Months')

    # Draw bar plot
    fig = facet_grid.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename(columns = {'value' : 'views'}, inplace=True)

    # Draw box plots (using Seaborn)
    fig, (year_ax, month_ax) = plt.subplots(nrows=1, ncols=2)

    fig.set_size_inches((20, 10))
    fig.set_dpi(100)

    sns.boxplot(
        data=df_box,
        x='year',
        y='views',
        ax = year_ax
    ).set_title(label = "Year-wise Box Plot (Trend)" )
    year_ax.set_ylabel("Page Views")
    year_ax.set_xlabel('Year')

    sns.boxplot(
        data = df_box,
        x = 'month',
        y= 'views',
        ax = month_ax,
        order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ).set_title(label="Month-wise Box Plot (Seasonality)")
    month_ax.set_ylabel('Page Views')
    month_ax.set_xlabel('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()

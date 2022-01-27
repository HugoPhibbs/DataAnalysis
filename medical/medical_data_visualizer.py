import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


def bmi(height, weight):
    return weight / (height ** 2)


def is_overweight(height, weight):
    return bmi(height, weight) > 25


# Import data
med_df = pd.read_csv(
    'medical_examination.csv'
)

# Add 'overweight' column
med_df['overweight'] = is_overweight(med_df['height'] / 100, med_df['weight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
med_df.loc[med_df['gluc'] == 1, 'gluc'] = 0
med_df.loc[med_df['gluc'] > 1, 'gluc'] = 1
med_df.loc[med_df['cholesterol'] == 1, 'cholesterol'] = 0
med_df.loc[med_df['cholesterol'] > 1, 'cholesterol'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = med_df.melt(
        id_vars='cardio',
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.value_counts().to_frame()
    df_cat.reset_index(inplace=True)
    df_cat.rename(columns={0: 'total'}, inplace=True)
    df_cat.sort_values(by='variable', inplace=True)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable',
                      y='total',
                      col='cardio',
                      data=df_cat,
                      legend=True,
                      hue='value',
                      kind='bar'
                      )

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    # Cleaning data
    heat_df = med_df[med_df['ap_lo'] <= med_df['ap_hi']]

    def remove_outliers(df: DataFrame, col: str):
        """
        Removes outliers from a dataframe by deleting entries bellow the 2.5% percentile
        and above the 97.5% percentile for a given column.

        :param df: DataFrame object to be cleaned
        :param col: string for column to be cleaned according to
        :return: adjusted dataframe
        """
        df = df[(df[col] >= df[col].quantile(0.025)) & (df[col] <= df[col].quantile(0.975))]
        return df

    df_heat = heat_df[(heat_df['ap_lo'] <= heat_df['ap_hi']) &
                 (heat_df['height'] >= heat_df['height'].quantile(0.025)) &
                 (heat_df['height'] <= heat_df['height'].quantile(0.975)) &
                 (heat_df['weight'] >= heat_df['weight'].quantile(0.025)) &
                 (heat_df['weight'] <= heat_df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    #corr_mat = heat_df.corr().round(decimals = 1)

    corr_mat = heat_df.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr_mat.shape)).astype(bool)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (15, 15))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data = corr_mat,
                ax = ax,
                annot = True,
                mask = mask,
                cmap = 'inferno',
                linewidths = 1,
                fmt = '.1f'
                )

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()
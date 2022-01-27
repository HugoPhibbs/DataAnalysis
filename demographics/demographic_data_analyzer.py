import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    demo_df = pd.read_csv(
        filepath_or_buffer="adult.data.csv"
    )

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = demo_df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(demo_df.loc[demo_df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(demo_df[demo_df['education'] == "Bachelors"].shape[0] / demo_df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_mask = (demo_df['education'] == "Bachelors") | (demo_df['education'] == "Masters") | (demo_df['education'] == "Doctorate")

    # percentage with salary >50K
    sal_mask = demo_df['salary'] == ">50K"
    higher_education_rich = round(demo_df.loc[edu_mask & sal_mask].shape[0] / demo_df[edu_mask].shape[0] * 100, 1)
    lower_education_rich = round(demo_df.loc[~edu_mask & sal_mask].shape[0] / demo_df.loc[~edu_mask].shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = demo_df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_mask = demo_df['hours-per-week'] == min_work_hours
    min_workers_rich_perc = round(demo_df[min_hours_mask & sal_mask].shape[0] / demo_df[min_hours_mask].shape[0] * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    perc_high_earners_per_country = round(demo_df.loc[sal_mask]['native-country'].value_counts().sort_index() / demo_df['native-country'].value_counts().sort_index() * 100, 1)
    highest_earning_country_percentage = perc_high_earners_per_country.max()
    highest_earning_country = perc_high_earners_per_country[perc_high_earners_per_country == highest_earning_country_percentage].index[0]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = demo_df.loc[sal_mask & (demo_df['native-country'] == 'India')]['occupation'].mode()[0]


    higher_education_rich

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {min_workers_rich_perc}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': min_workers_rich_perc,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()

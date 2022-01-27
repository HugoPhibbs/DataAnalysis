import pandas as pd

med_df = pd.read_csv('medical_examination.csv')

def bmi(height, weight):
    return weight / (height**2)


def is_overweight(height, weight):
    return bmi(height, weight) > 25

med_df['overweight'] = is_overweight(med_df['height'], med_df['weight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
med_df[med_df['gluc'] > 1] = 1
med_df[med_df['cholesterol'] > 1] = 1


med_df = med_df.melt(
    id_vars='cardio',
    value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

#med_df = med_df.groupby(['cardio', 'variable', 'value'], group_keys=False).mean()

print(med_df.index.names)

med_df = med_df.value_counts().to_frame()
med_df.reset_index(inplace = True)
med_df.rename(columns = {'value' : 'total', 0:'count'}, inplace = True)

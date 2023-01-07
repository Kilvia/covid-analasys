import pandas as pd

data = pd.read_csv('time_series_covid19_confirmed_global.csv')

# Group the DataFrame by Province/State and Country/Region
grouped_df = data.groupby(['Country/Region'])

# Apply the sum function to the grouped data
summed_df = grouped_df.sum()
summed_df = summed_df.drop(['Lat', 'Long'], axis=1)
print(summed_df)
import pandas as pd
import matplotlib.pyplot as plt

# Load an explore the data
data = pd.read_csv("housing.csv", sep=',')
print(data.head())
data.info()

# 1. How many geographical units are there in the dataset?
# I consider geographical units unique combinations of lat and len
unique_units = data[['longitude','latitude']].drop_duplicates() # get only lon and lat columns and remove duplicate rows
print(f'1. There are {len(unique_units)} geographical units in the dataset.')

# 2. What is the mean house value among all “Ocean_proximity” categories?
housev_mean = data[['median_house_value']].mean().rename({"median_house_value": "Mean (median) house value"})
print(f'2. The mean house value among all "Ocean proximity" categories is {housev_mean.iloc[0]}.')

# 3. What is the mean house value in each “Ocean_proximity” category?
housev_mean_cat = data[['median_house_value', 'ocean_proximity']].groupby(['ocean_proximity']).mean().rename(columns={"median_house_value": "Mean (median) house value"})
print(f'3. The mean house values in each "Ocean proximity" categories are:\n{housev_mean_cat}')

# 4. What can you tell about the differences between the mean and median values?
print('4. The median is less sensitive about outliers, as it is the middle value after sorting')

# 5. Create histograms for the following columns: “households”, “median_income”, “housing_median_age” and “median_house_value”.
count = data[['households', 'median_income', 'housing_median_age', 'median_house_value']].groupby
plt.bar(data['households'])
plt.show()
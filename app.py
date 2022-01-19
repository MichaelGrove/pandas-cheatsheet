import numpy as np
import pandas as pd

# Read CSV. First row should be concidered as header
#df = pd.read_csv('example.csv', delimiter=';', header=0)

# Read CSV. Assign headers for columns manually.
df = pd.read_csv('example.csv', delimiter=';', header=0,
                 names=["year", "brand", "model", "length"])


df.dropna(subset=['year'], inplace=True)

# Visualize dataframe
# print(df.head())

# Print shape of dataframe eg. number of columns and rows
# print(df.shape)

# Print all values from single column
# print(df["model"])

# Print first row
# print(df.iloc[0])

# Print column value from first row
# print(df.iloc[0]["model"])

# Print rows where column value is equal to another value
# print(df.loc[df['brand'] == "Peugeot"])

# Drop empty lines without a valid year
# df.dropna(subset=['year'], inplace=True)
# print(df.head())

# Convert dataframe column value to int
# and print values that are greater than another value
# print(df.loc[df['year'] < 2010])

# Map column values
# df['year'] = df['year'].map(lambda val: val + 1 if val < 2010 else val - 1)
# print(df.head())

# Add column based on other column values
# df['brand-model'] = df.apply(lambda row: str(row.brand) +
#                              " - " + str(row.model), axis=1)
# print(df.head())

# Filter dataframe by value comparison
# df = df[df['year'] < 2010]
# print(df.head())

# Drop rows by value comparison
# df.drop(df[df['year'] < 2010].index, inplace=True)
# print(df.head())

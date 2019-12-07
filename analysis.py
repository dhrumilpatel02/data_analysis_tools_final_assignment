# Import Libraries
import pandas as pd
import matplotlib as plt
%matplotlib inline

# Read CSV and store in two different dataframes
df = pd.read_csv('survey.csv')
fd = pd.read_csv('survey.csv')

# Print first five values to see the whole dataset
print(df.head())
print(fd.head())

# Rename seek_help and treatment's Categorical values to Numerical values for smoother filtering
df["seek_help"] = df["seek_help"].replace(["Yes", "Don't know", "No"], [1, 0.5, 0])
df = df[df.seek_help==1]

fd["treatment"] = fd["treatment"].replace(["Yes", "No"], [1, 0]) 
fd = fd[fd.treatment==1]

# Filtering out null values from the column 'state' and selected the country as USA
df = df[df['state'].notnull()]
df = df[df.Country=='United States']

fd = fd[fd['state'].notnull()]
fd = fd[fd.Country=='United States']

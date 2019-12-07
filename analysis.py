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

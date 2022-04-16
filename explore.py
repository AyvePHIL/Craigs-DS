# Working packages
import plotly.express as px
import pandas as pd
import numpy as np
import pandas_profiling
from IPython.display import display
from pandas_profiling import ProfileReport
import seaborn as sns

#DATA PROCESSING
df = pd.read_csv("data.csv")
# display(df.head(5))

#check number of empty or missing values in each column
craig = df.isnull().sum()
# print(craig)

df2 = df.dropna()

# display(df2.head(15))
# print(df2.isnull().sum())
# perform complete dataframe inspection report for 
# explore = ProfileReport(df, title="Data File Inspection", html={
#                         'style': {'full_width': True}})
# explore.to_file("explore_data2.html")

# EXPLORE DATA


# CONCLUSION


#ANSWERS
fig = px.scatter(x=df["Country"], y=df["Under15"])
# fig.show()
df_find_country = df.loc[df['Under15'] == min(df['Under15'])]

print("3: Therefore the country is " + df_find_country['Country'])

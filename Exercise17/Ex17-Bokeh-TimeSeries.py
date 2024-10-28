from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
import pandas as pd

#read the csv file into a pandas dataframe
abnd_df = pd.read_csv('ABND.csv')
amzn_df = pd.read_csv('AMZN.csv')
goog_df = pd.read_csv('GOOG.csv')

#convert the date values to datetime type
abnd_df['Date'] = pd.to_datetime(abnd_df['Date'])
amzn_df['Date'] = pd.to_datetime(amzn_df['Date'])
goog_df['Date'] = pd.to_datetime(goog_df['Date'])

#print the first few rows of the dataframe and the data types of the columns
print(abnd_df.head())
print(abnd_df.dtypes)
print(amzn_df.head())
print(amzn_df.dtypes)
print(goog_df.head())
print(goog_df.dtypes)
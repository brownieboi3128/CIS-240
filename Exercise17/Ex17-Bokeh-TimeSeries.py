from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
import pandas as pd

#read the csv file into a pandas dataframe
abnd = pd.read_csv('ABND.csv')
amzn = pd.read_csv('AMZN.csv')
goog = pd.read_csv('GOOG.csv')

#convert the date values to datetime type
abnd['Date'] = pd.to_datetime(abnd['Date'])
amzn['Date'] = pd.to_datetime(amzn['Date'])
goog['Date'] = pd.to_datetime(goog['Date'])

#print the first few rows of the dataframe and the data types of the columns
print(abnd.head())
print(abnd.dtypes)
print(amzn.head())
print(amzn.dtypes)
print(goog.head())
print(goog.dtypes)
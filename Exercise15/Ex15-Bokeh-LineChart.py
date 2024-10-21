import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout

df = pd.read_csv('europe_tourism.csv')
print(df)
# Output to an HTML File
output_file('Ex15-Bokeh-LineChart.html')

# ColumnDataSource object
tourism_source = ColumnDataSource(df)

# Instantiate the figure object
fig = figure(title='International Tourist Arrivals (millions)',
             x_axis_label='Year',
             y_axis_label='Tourists',
             background_fill_color='rgb(193, 168, 117)',)

# Line method
fig.line(x= 'Year', 
         y = 'Western',
         source = tourism_source, 
         line_width=5, 
         color='green',
         line_dash='dashed',
         legend_label='Western Europe')
fig.line(x= 'Year', 
         y = 'Eastern',
         source = tourism_source, 
         line_width=5, 
         color='red',
         line_dash='dotted',
         legend_label='Eastern Europe')
fig.line(x= 'Year', 
         y = 'Southern',
         source = tourism_source, 
         line_width=5, 
         color='blue',
         line_dash='solid',
         legend_label='Southern Europe')


full_fig = layout([[fig]], sizing_mode='stretch_both')
show(full_fig)

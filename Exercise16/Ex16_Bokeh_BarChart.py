from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
import pandas as pd

#load data
apparel_df = pd.read_csv('Apparel16.csv')

# Create a ColumnDataSource object
apparel_source = ColumnDataSource(apparel_df)
apparel = apparel_df['Apparel']

# Instantiate the figure object with the x_range
fig = figure(x_range = apparel_df['Apparel'], 
             title='Apparel Sales by Type and Year',
             tools = 'hover', 
             tooltips = '@apparel: @$name')

# Create a stacked bar chart for the years 2026 and 2027 
fig.vbar_stack(['2026', '2027'],
                x = 'Apparel', 
                width = 0.9,
                color = ('#592C88FF', '#C1A875FF'),
                source = apparel_source,
                legend_label = ['2026', '2027']
                )    


#---Snip---
fig.yaxis.formatter.use_scientific = False

# Increase the size of the axes labels
fig.xaxis.major_label_text_font_size = "30pt"
fig.yaxis.major_label_text_font_size = "20pt"

# Increase the title font size, and set the legend location
fig.title.text_font_size = "25pt"
fig.legend.location = "top_left"
fig.legend.orientation = "horizontal"

# Show the figure 
full_fig = layout([[fig]], sizing_mode='stretch_both')
show(full_fig)

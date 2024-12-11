from django.shortcuts import render
from .models import Product
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

# Create your views here.
def bar_chart(request):
    products = Product.objects.all()
    products_price = [(product.name, product.price) for product in products]
    df = pd.DataFrame(products_price, columns=['Product', 'Price'])
    # Instantiate the figure object
    fig = figure(x_range=df['Product'], title='Product Prices', width=700, height=500)
    # Create a bar chart
    fig.vbar(source=df, x='Product', top='Price', width=0.5, color='navy')
    html, div = components(fig)
    context = {'html': html, 'div': div}
    return render(request, 'exam_app/bar_chart.html', context)
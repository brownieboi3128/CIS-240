from django.contrib import admin

# Register your models here.
from exam_app.models import Category
from exam_app.models import Product

admin.site.register(Category)
admin.site.register(Product)
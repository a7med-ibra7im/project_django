from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
admin.site.site_header = 'Ahmed'



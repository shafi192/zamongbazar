from django.contrib import admin
from . models import  Product, Sub_category, Sub_product,Vendor,Contact,Front,Market
# Register your models here.
admin.site.register(Sub_category)
admin.site.register(Product)
admin.site.register(Sub_product)
admin.site.register(Vendor)
admin.site.register(Contact)
admin.site.register(Front)
admin.site.register(Market)
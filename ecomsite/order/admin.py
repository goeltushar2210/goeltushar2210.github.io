from django.contrib import admin
from .models import *

class ShopCartAdmin(admin.ModelAdmin):
    list_display = [ 'product','quantity','price','amount']
    list_filter = ['user']

admin.site.register(ShopCart,ShopCartAdmin)
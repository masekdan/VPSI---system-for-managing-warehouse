from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Warehouse)
admin.site.register(Stocks)
admin.site.register(StocksHistory)

admin.site.register(UserConfig)
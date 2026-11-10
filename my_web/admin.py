
from django.contrib import admin
from .models import Category, Dish, Table, Order, OrderItem

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)

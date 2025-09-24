# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email',
                    'county', 'pickup_station', 'payment_method', 'paid', 'created']
    list_filter = ['paid', 'created', 'updated', 'payment_method']
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']

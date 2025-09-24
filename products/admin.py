from django.contrib import admin
from .models import Product, ProductVariant

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1  # how many empty rows you want by default


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductVariantInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'price', 'icing', 'egg_option']
    list_filter = ['icing', 'egg_option']

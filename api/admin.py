from django.contrib import admin

from .models import Category, Products, Order, Trdelnik
# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('quantity', )


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Trdelnik)

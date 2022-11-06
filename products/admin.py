from django.contrib import admin
from .models import Product, Category, Scent

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ScentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'scent',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Scent, ScentAdmin)

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('id',)
    list_per_page = 20

    fieldsets = (
        ('Información Principal', {
            'fields': ('name', 'description', 'price')
        }),
        ('Categorización', {
            'fields': ('category', 'features')
        }),
        ('Imagen', {
            'fields': ('image_url',)
        }),
    )

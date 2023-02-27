from django.contrib import admin
from .models import Product, Brand, Variation, ProductGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'in_stock')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductGalleryInline]

    class Meta:
        model = Product

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

    class Meta:
        model = Variation

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ProductGallery)


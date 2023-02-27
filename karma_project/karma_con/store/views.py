from django.shortcuts import render
from .models import Product, Brand , ProductGallery , Variation
from django.views.generic import ListView


def store(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'products': products,
        'brands': brands
    }
    return render(request, 'store.html', context)

def brand_list(request, brand_slug):
    products = Product.objects.all().filter(brand__slug=brand_slug)
    brands = Brand.objects.all()
    context = {
        'products': products,
        'brands': brands
    }
    return render(request, 'store.html', context)

def product(request,product_id):
    product = Product.objects.get(id=product_id)
    product_gallery = ProductGallery.objects.filter(product=product)
    variations = Variation.objects.filter(product=product)
    context = {
        'product': product,
        'product_gallery': product_gallery,
        'variations': variations
    }
    return render(request, 'product.html', context )
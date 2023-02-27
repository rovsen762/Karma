from django.db import models
from django.urls import reverse

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    verbose_name = 'Brand'
    verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    information = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    verbose_name = 'Product'
    verbose_name_plural = 'Products'

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product', args=[self.slug])

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={ 'slug': self.slug })

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=50, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    verbose_name = 'Variation'
    verbose_name_plural = 'Variations'

    def __str__(self):
        return self.variation_value

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', blank=True)

    verbose_name = 'Product Gallery'
    verbose_name_plural = 'Product Galleries'

    def __str__(self):
        return self.product.name

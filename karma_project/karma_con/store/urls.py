from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('brands/<slug:brand_slug>/', views.brand_list, name='products_by_brand'),
    path('<int:product_id>/', views.product, name='product'),
]

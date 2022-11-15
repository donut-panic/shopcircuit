from django.template.defaulttags import url
from django.urls import path

from store.views import StoreMainView, StoreCategoryView, ProductView, AddProductToCartView, CartView

app_name = "store"

urlpatterns = [
    path("", StoreMainView.as_view(), name="store_main_view"),
    path("category/<pk>", StoreCategoryView.as_view(), name="category_view"),
    path("product/<pk>", ProductView.as_view(), name="product_view"),
    path("cart/add/<pk>", AddProductToCartView.as_view(), name="add_product_to_cart_view"),
    path("cart/", CartView.as_view(), name="cart_view"),
]
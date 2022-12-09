from django.urls import path

from store.views import StoreMainView, StoreCategoryView, ProductView, AddProductToCartView, CartView, \
    DeleteFromCartView, IncreaseQuantityInCart, DecreaseQuantityInCart, LeStoreCategoryView, SearchView, \
    WishlistView, AddToWishlistView, DeleteFromWishlistView

app_name = "store"

urlpatterns = [
    path("", StoreMainView.as_view(), name="store_main_view"),
    path("category/<pk>", StoreCategoryView.as_view(), name="category_view"),
    path("product/<pk>", ProductView.as_view(), name="product_view"),
    path("subcategory/<pk>", LeStoreCategoryView.as_view(), name="leproduct_view"),
    path("cart/add/<pk>", AddProductToCartView.as_view(), name="add_product_to_cart_view"),
    path("cart/", CartView.as_view(), name="cart_view"),
    path("cart/delete/<pk>", DeleteFromCartView.as_view(), name="delete_from_cart_view"),
    path("cart/increase/<pk>", IncreaseQuantityInCart.as_view(), name="increase_quantity_in_cart_view"),
    path("cart/decrease/<pk>", DecreaseQuantityInCart.as_view(), name="decrease_quantity_in_cart_view"),
    path("search/", SearchView.as_view(), name="search_products"),
    path("wishlist/", WishlistView.as_view(), name='wishlist_view'),
    path("wishlist/add/<int:pk>", AddToWishlistView.as_view(), name='add_to_wishlist_view'),
    path("wishlist/delete/<int:pk>", DeleteFromWishlistView.as_view(), name='delete_from_wishlist_view'),
]

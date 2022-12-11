from random import sample
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from store.models import Product, Category, UnitOrder, Subcategory, WishlistItem


class StoreMainView(View):
    """Main view for the store."""
    def get(self, request):
        categories = []
        random_categories = sample(list(Category.objects.all()), 4)
        for category in random_categories:
            categories.append({
                "id": category.id,
                "name": category.name,
                "products": Product.objects.filter(category=category.id)[:4]
            })
        return render(
            request,
            template_name="main/store_main_view.html",
            context={
                "random_categories": categories
            }
        )


class CategoryView(View):
    """View for displaying category."""
    def get(self, request, pk):
        return render(
            request,
            template_name="category/category_view.html",
            context={
                "products_list": Product.objects.filter(category_id=pk),
                "category": Category.objects.get(id=pk),
                "subcategories": Subcategory.objects.filter(category_id_id=pk),
            }
        )


class SubcategoryView(View):
    """View for displaying subcategory."""
    def get(self, request, pk):
        return render(
            request,
            template_name="category/category_view.html",
            context={
                "products_list": Product.objects.filter(subcategory_id=pk),
                "category": Subcategory.objects.get(id=pk),
            }
        )


class ProductView(DetailView):
    """Detailed view for the product page."""
    model = Product
    template_name = "product/product_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = UnitOrder.objects.filter(product_id=self.get_object()).count()
        context["category"] = Category.objects.get(id=self.get_object().category.id)
        context["subcategory"] = Subcategory.objects.get(id=self.get_object().subcategory.id)
        context["similar_products"] = Product.objects.filter(category=self.object.category).exclude(id=self.object.id)[:4]
        return context


class AddProductToCartView(View):
    """View for adding products to the shopping cart."""
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            pk = str(product.id)
            cart = request.session.get("cart")
            if cart:
                if pk in cart:
                    cart[pk] += 1
                else:
                    cart.update({pk: 1})
                request.session["cart"] = cart
            else:
                request.session["cart"] = {pk: 1}
            return redirect("store:cart_view")
        except Product.DoesNotExist:
            return HttpResponse("sorry but this item does not exists")


class CartView(View):
    """Main view for displaying cart."""
    def get(self, request):
        cart_summary = []
        cart = request.session.get("cart")
        total_price = 0
        total_tax = 0
        if cart:
            total_price = 0
            products_in_cart = Product.objects.select_related("category").filter(id__in=request.session["cart"].keys())
            for product in products_in_cart:
                quantity = cart[str(product.id)]
                product_total_price = product.price * quantity
                tax = (product_total_price * product.tax)
                cart_summary.append({
                    "product": product,
                    "quantity": quantity,
                    "total_price": product_total_price,
                    "tax": tax
                })
                total_price += product_total_price
                total_tax += tax
        return render(
            request,
            template_name="cart/cart_view.html",
            context={
                "products": cart_summary if len(cart_summary) > 0 else None,
                "total_price": total_price,
                "total_tax": total_tax
            }
        )


class DeleteFromCartView(View):
    """View for deleting product from cart."""
    def get(self, request, pk):
        try:
            cart = request.session["cart"]
            cart.pop(pk)
            request.session["cart"] = cart
            return redirect("store:cart_view")
        except KeyError:
            return HttpResponse("can't remove product that is not in the cart")


class IncreaseQuantityInCart(View):
    """View for increasing product quantity in cart."""
    def get(self, request, pk):
        cart = request.session.get("cart")
        try:
            product = Product.objects.get(id=pk)
            if cart and pk in cart:
                if cart[pk] + 1 <= product.quantity:
                    cart[pk] += 1
            request.session["cart"] = cart
            return redirect("store:cart_view")
        except Product.DoesNotExist:
            return HttpResponse("no such product so cant increase")


class DecreaseQuantityInCart(View):
    """View for decreasing product quantity in cart."""
    def get(self, request, pk):
        cart = request.session.get("cart")
        try:
            product = Product.objects.get(id=pk)
            if cart and pk in cart:
                if cart[pk] - 1 < 1:
                    cart.pop(pk)
                else:
                    cart[pk] -= 1
            request.session["cart"] = cart
            return redirect("store:cart_view")
        except Product.DoesNotExist:
            return HttpResponse("no such product so cant increase")


class SearchView(ListView):
    """The main view for displaying searching results."""
    template_name = "search/search_view.html"
    model = Product
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.select_related("category", "subcategory").all()
        keywords = self.request.GET.get("keywords")
        category_id = self.request.GET.get("category_id")
        if category_id != "":
            queryset = queryset.filter(category=int(category_id))
        if len(keywords) > 0:
            queryset = queryset.filter(name__icontains=keywords)
        else:
            queryset = queryset.none()
        return queryset


class WishlistView(LoginRequiredMixin, ListView):
    """Main view for displaying the wishlist."""
    template_name = "wishlist/wishlist_view.html"

    def get_queryset(self):
        wishlisted_items = WishlistItem.objects.select_related('product').filter(user=self.request.user)
        return [wishlisted_item.product for wishlisted_item in wishlisted_items]


class AddToWishlistView(LoginRequiredMixin, View):
    """Adds new WishlistItem object to database."""
    def get(self, request, pk):
        added_product = get_object_or_404(Product, pk=pk)
        if added_product:
            if not WishlistItem.objects.filter(user=request.user, product=added_product).exists():
                WishlistItem(user=request.user, product=added_product).save()
        return redirect("store:wishlist_view")


class DeleteFromWishlistView(LoginRequiredMixin, View):
    """Removes WishlistItem object from database."""
    def get(self, request, pk):
        wishlist_item = get_object_or_404(WishlistItem, user=request.user.id, product_id=pk)
        wishlist_item.delete()
        return redirect("store:wishlist_view")

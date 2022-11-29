from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from store.models import Product, Category, UnitOrder, LeCategory, Wishlist


class StoreMainView(View):
    def get(self, request):
        random_categories = sample(list(Category.objects.all()), 4)
        context = []
        for i in random_categories:
            context.append({
                "name": i.name,
                "products": Product.objects.filter(category=i.id)[:4]
            })
        return render(
            request,
            template_name="main/store_main_view.html",
            context={
                "random_categories": context
            }
        )


class StoreCategoryView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="category/category_view.html",
            context={
                "products_list": Product.objects.filter(category_id=pk),
                "category": Category.objects.get(id=pk),
                "lecategories": LeCategory.objects.filter(category_id_id=pk),
            }
        )


class LeStoreCategoryView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name='subcategory/subcategory_view.html',
            context={
                "products_list": Product.objects.filter(subcategory_id=pk),
                "lecategory": LeCategory.objects.get(id=pk),
                "lecategories_list": LeCategory.objects.filter(category_id_id=pk),
            }
        )


class ProductView(DetailView):
    model = Product
    template_name = "product/product_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["orders"] = UnitOrder.objects.filter(product_id=self.get_object()).count()
        context["category"] = Category.objects.get(id=self.get_object().category.id)
        context["subcategory"] = LeCategory.objects.get(id=self.get_object().subcategory.id)
        return context


class AddProductToCartView(View):
    def get(self, request, pk):
        cart = request.session.get("cart")
        if cart:
            for item in cart:
                if item["id"] == pk:
                    item["quantity"] += 1
                    break
            else:
                cart.append({"id": pk, "quantity": 1})
            request.session["cart"] = cart
        else:
            request.session["cart"] = [{"id": pk, "quantity": 1}]
        return redirect("store:cart_view")


class CartView(View):
    def get(self, request):
        in_cart = []
        overall_price = 0
        overall_tax = 0
        if "cart" in request.session:
            overall_price = 0
            for item in request.session["cart"]:
                product = Product.objects.select_related("category").get(id=item["id"])
                total_price = product.price * item["quantity"]
                tax = (total_price * product.tax)
                in_cart.append({
                    "product": product,
                    "quantity": item["quantity"],
                    "total_price": total_price,
                    "tax": tax
                })
                overall_price += total_price
                overall_tax += tax


        return render(
            request,
            template_name="cart/cart_view.html",
            context={
                "products": in_cart if len(in_cart) > 0 else None,
                "overall_price": overall_price,
                "overall_tax": overall_tax
            }
        )


class DeleteFromCartView(View):
    def get(self, request, pk):
        cart = request.session["cart"]
        request.session["cart"] = [item for item in cart if item["id"] != pk]
        return redirect("store:cart_view")


class IncreaseQuantityInCart(View):
    def get(self, request, pk):
        cart = request.session["cart"]
        for item in cart:
            if item["id"] == pk:
                item["quantity"] -= 1
        request.session["cart"] = [item for item in cart if item["quantity"] > 0]
        return redirect("store:cart_view")


class DecreaseQuantityInCart(View):
    def get(self, request, pk):
        cart = request.session["cart"]
        for item in cart:
            if item["id"] == pk:
                item["quantity"] += 1
        request.session["cart"] = cart
        return redirect("store:cart_view")


def search_venues(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        venues = Product.objects.filter(name__icontains=searched)
        return render(request,
                      'search_product/search_view.html', {'searched': searched, 'venues': venues})
    else:
        return render(request,
                      'search_product/search_view.html', {})


class SearchView(ListView):
    template_name = "search_product/search_view.html"
    model = Product
    paginate_by = 20

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


class WishlistView(LoginRequiredMixin, View):
    def get(self, request):
        users_wishlist = Wishlist.objects.get(user=request.user.id)
        wishlist_content = [int(i) for i in users_wishlist.get_products()["products"]]
        return render(
            request,
            template_name="wishlist/wishlist_view.html",
            context={"wishlist": Product.objects.filter(pk__in=wishlist_content)}
        )


class AddToWishlistView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user_wishlist = Wishlist.objects.get(user=request.user.id)
        wishlist_content = user_wishlist.get_products()
        if pk not in wishlist_content["products"]:
            wishlist_content["products"].append(pk)
        user_wishlist.set_products(wishlist_content)
        user_wishlist.save()
        return redirect("store:wishlist_view")


class DeleteFromWishlistView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user_wishlist = Wishlist.objects.get(user=request.user.id)
        wishlist_content = user_wishlist.get_products()
        if pk in wishlist_content["products"]:
            wishlist_content["products"].remove(pk)
        user_wishlist.set_products(wishlist_content)
        user_wishlist.save()
        return redirect("store:wishlist_view")
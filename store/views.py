from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView

from store.models import Product, Category, UnitOrder, LeCategory


class StoreMainView(TemplateView):
    template_name = "base.html"


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
        context["orders"] = UnitOrder.objects.filter(product_id=self.get_object()).count()
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
        venues = Product.objects.filter(name=searched)
        return render(request,
                      'search_product/search_product.html', {'searched': searched, 'venues': venues})
    else:
        return render(request,
                      'search_product/search_product.html', {})
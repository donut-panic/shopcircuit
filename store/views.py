from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView

from store.models import Product, UnitOrder, TypeProduct, SubTypeProduct


class StoreMainView(TemplateView):
    template_name = "base.html"


class StoreCategoryView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="category/category_view.html",
            context={
                "products_list": Product.objects.filter(category_id=pk),
                "category": TypeProduct.objects.get(id=pk),
                "categories": TypeProduct.objects.filter(parent_id__isnull=True),
                "subcategories": SubTypeProduct.objects.filter(parent_id=pk),
                "cart": len(request.session["cart"]) if "cart" in request.session else 0
            }
        )


class ProductView(DetailView):
    model = Product
    template_name = "product/product_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = TypeProduct.objects.all()
        context["orders"] = UnitOrder.objects.filter(product_id=self.get_object()).count()
        context["cart"] = len(self.request.session["cart"]) if "cart" in self.request.session else 0
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
        if "cart" in request.session:
            cart = request.session["cart"]
        return render(
            request,
            template_name="cart/cart_view.html",
            context={
                "cart": len(request.session["cart"]) if "cart" in request.session else 0,
                "cart_content": cart

            }
        )
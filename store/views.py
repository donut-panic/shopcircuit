from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from store.models import Product, Category


class StoreMainView(TemplateView):
    template_name = "base.html"


class StoreCategoryView(View):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        return render(
            request,
            template_name="category_view.html",
            context={"products_list": Product.objects.filter(category_id=pk), "category": category}
        )

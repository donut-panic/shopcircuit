from django.template.defaultfilters import register

from store.models import Category, LeCategory


def get_categories(request):
    return {
        "categories": Category.objects.all(),
        "subclasses": LeCategory.objects.all()
    }

def get_number_of_items_in_cart(request):
    if "cart" in request.session:
        return {"cart_items_number": len(request.session["cart"])}
    return {"cart_items_number": 0}



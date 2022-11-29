from django.template.defaultfilters import register

from store.models import Category, LeCategory, Wishlist


def get_categories(request):
    return {
        "categories": Category.objects.all(),
        "subclasses": LeCategory.objects.all()
    }


def get_number_of_items_in_cart(request):
    if "cart" in request.session:
        return {"cart_items_number": len(request.session["cart"])}
    return {"cart_items_number": 0}


def get_wishlist_content(request):
    if request.user.is_authenticated:
        users_wishlist = Wishlist.objects.get(user=request.user.id)
        wishlist_content = [int(i) for i in users_wishlist.get_products()["products"]]
        return {"wishlist_content": wishlist_content}
    return {"wishlist_content": []}

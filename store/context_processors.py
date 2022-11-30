from django.template.defaultfilters import register

from store.models import Category, LeCategory, Wishlist


def get_categories(request):
    parents_id_that_have_childs = LeCategory.objects.filter(category_id_id__isnull=False).values_list('category_id_id',
                                                                                                      flat=True)
    categories_with_subcategories = Category.objects.filter(id__in=list(set(parents_id_that_have_childs)))
    categories_all = Category.objects.all()
    categories_without_subcategories = categories_all.difference(categories_with_subcategories)
    return {
        "categories": categories_with_subcategories,
        "single_categories": categories_without_subcategories
    }


def get_subclasses(request):
    subclasses = LeCategory.objects.all()
    if subclasses:
        return {"subclasses": subclasses}
    return {}



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

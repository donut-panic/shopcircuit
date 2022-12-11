from store.models import Category, Subcategory, WishlistItem


def get_categories(request):
    parents_id_that_have_childs = Subcategory.objects.filter(category_id_id__isnull=False).values_list('category_id_id',
                                                                                                      flat=True)
    categories_with_subcategories = Category.objects.filter(id__in=list(set(parents_id_that_have_childs)))
    categories_all = Category.objects.all()
    categories_without_subcategories = categories_all.difference(categories_with_subcategories)
    return {
        "categories": categories_with_subcategories,
        "single_categories": categories_without_subcategories
    }


def get_subclasses(request):
    """Retrieves subcategories."""
    subclasses = Subcategory.objects.all()
    if subclasses:
        return {"subclasses": subclasses}
    return {}


def get_number_of_items_in_cart(request):
    """Retriever number of items in cart."""
    if "cart" in request.session:
        return {"cart_items_number": len(request.session["cart"])}
    return {"cart_items_number": 0}


def get_wishlist_content(request):
    """Retrieves wishlisted products for authenticated user."""
    if request.user.is_authenticated:
        wishlisted_items = WishlistItem.objects.select_related('product').filter(user=request.user)
        return {"wishlist_content": [wishlisted_item.product for wishlisted_item in wishlisted_items]}
    return {"wishlist_content": []}

from store.models import Product


def sidepanel(request):
    in_cart = []
    overall_price = 0
    overall_tax = 0
    if "cart" in request.session:
        overall_price = 0
        for (product_id, quantity) in request.session["cart"].items():
            product = Product.objects.select_related("category").get(id=product_id)
            total_price = product.price * quantity
            tax = (total_price * product.tax)
            in_cart.append({
                "product": product,
                "quantity": quantity,
                "total_price": total_price,
                "tax": tax
            })
            overall_price += total_price
            overall_tax += tax
        return {"sidepanel_products": in_cart if len(in_cart) > 0 else None,
                "sidepanel_overall_price": overall_price,
                "sidepanel_overall_tax": overall_tax}
    return {}






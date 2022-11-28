from store.models import Product


def sidepanel(request):
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
        return {"sidepanel_products": in_cart if len(in_cart) > 0 else None,
                "sidepanel_overall_price": overall_price,
                "sidepanel_overall_tax": overall_tax}
    return {}






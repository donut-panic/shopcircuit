from random import sample

from django.http import request
from django.shortcuts import render

from store.models import Product
from .models import Profile


def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.image
        return {'picture_profile': pic}
    return {}


# def product(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     recently_viewed_products = None
#
#     if 'recently_viewed' in request.session:
#         if product_id in request.session['recently_viewed']:
#             request.session['recently_viewed'].remove(product_id)
#         products = Product.objects.filter(pk__in=request.session['recently_viewed'])
#         recently_viewed_products = sorted(products,
#             key=lambda x: request.session['recently_viewed'].index(x.id)
#             )
#         request.session['recently_viewed'].insert(0, product_id)
#         if len(request.session['recently_viewed']) > 5:
#             request.session['recently_viewed'].pop()
#     else:
#         request.session['recently_viewed'] = [product_id]
#         random_categories = sample(list(Product.objects.all('category_id')), 4)
#         for i in range(4):
#             request.session['recently_viewed'].insert(-1, random_categories[i])
#             if len(request.session['recently_viewed']) > 5:
#                 request.session['recently_viewed'].pop()
#
#     request.session.modified = True
#
#     context = {'_product': product, 'recently_viewed_products': recently_viewed_products}
#     return render(request, 'recent.html', context)

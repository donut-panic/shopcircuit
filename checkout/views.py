from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from accounts.forms import LoginForm
from checkout.forms import AddOrderInfoForm
from store.models import Order, UnitOrder, Product


# Create your views here.


class CheckoutLoginView(LoginView):
    form_class = LoginForm
    template_name = 'order/login_checkout.html'
    success_url = 'order/order_view.html'
    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True
        return super(CheckoutLoginView, self).form_valid(form)

    def get_success_url(self):
        return '/checkout/order/'

class OrderView(CreateView):
    template_name = 'order/order_view.html'
    form_class = AddOrderInfoForm
    success_url = reverse_lazy('confirm_view')

    def get_initial(self):
        return {'order_by': self.request.user}

    def form_valid(self, form):
        form.cleaned_data.pop('order_by')
        obj, created = Order.objects.update_or_create(
            order_by=self.request.user, defaults=form.cleaned_data
        )
        return HttpResponseRedirect(self.success_url)


class PleaseLoginView(View):
    def get(self, request):
        return render(request, template_name='order/please_login.html', )


class ConfirmView(View):
    def get(self, request):
        return render(
            request,
            template_name="order/confirm.html",
            context={"confirms": Order.objects.all(),

                     }
        )


class CheckOutView(View):
    def get(self, request):
        if 'cart' in request.session:
            order_id = Order.objects.filter(order_by=self.request.user).values()[0].get('id')
            for item in request.session['cart']:
                product = Product.objects.select_related("category").get(id=item["id"])
                unitorder = UnitOrder(order_id_id=order_id,
                                      product_id=product,
                                      quantity=item["quantity"],
                                      price=product.price + product.tax
                                      )
                unitorder.save()
            unit_orders = UnitOrder.objects.filter(order_id=Order.objects
                                                   .filter(order_by=self.request.user).values()[0].get('id'))
            order_detail = Order.objects.filter(order_by=self.request.user)
            total_price = round(sum([float(i[0]) for i in list(unit_orders.values_list('price'))]),2)
            del request.session['cart']
            return render(request, 'final/final_view.html', {'unit_orders': unit_orders,
                                                             'total_price': total_price,
                                                             'order_detail': order_detail
                                                             }
                          )
        else:
            unit_orders = UnitOrder.objects.filter(order_id=Order.objects
                                                   .filter(order_by=self.request.user).values()[0].get('id'))
            total_price = round(sum([float(i[0]) for i in list(unit_orders.values_list('price'))]), 2)
            order_detail = Order.objects.filter(order_by=self.request.user)
            return render(request, 'final/final_view.html', {'unit_orders': unit_orders,
                                                             'total_price': total_price,
                                                             'order_detail': order_detail
                                                             }
                          )


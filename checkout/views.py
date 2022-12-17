from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import LoginForm
from accounts.models import Profile
from checkout.forms import AddOrderInfoForm
from store.models import Order, UnitOrder, Product, OrderStatus


class PleaseLoginView(View):
    """Login request view that is displayed when placing an order."""
    def get(self, request):
        return render(
            request,
            template_name="order/please_login.html"
        )


class CheckoutLoginView(LoginView):
    """Login view for checkout section."""
    form_class = LoginForm
    template_name = "order/login_checkout.html"
    success_url = "order/order_view.html"

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CheckoutLoginView, self).form_valid(form)

    def get_success_url(self):
        return "/checkout/order/"


class OrderView(LoginRequiredMixin, CreateView):
    """View for filling order form."""
    template_name = "order/order_view.html"
    form_class = AddOrderInfoForm
    success_url = reverse_lazy("confirm_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_profile"] = Profile.objects.get(user=self.request.user)
        return context

    def form_valid(self, form):
        context = super().get_context_data()
        form.instance.order_by = self.request.user
        form.instance.order_status = OrderStatus.objects.get(name="Pending")
        form.instance.phone = context["phone"]
        return super().form_valid(form)


class ConfirmView(View):
    def get(self, request):
        return render(
            request,
            template_name="order/confirm.html",
            context={
                "confirms": Order.objects.all()
            }
        )


class CheckOutView(View):
    def get(self, request):
        if "cart" in request.session:
            order_id = Order.objects.filter(order_by=self.request.user).values()[0].get("id")
            for item in request.session["cart"]:
                product = Product.objects.select_related("category").get(id=item["id"])
                unitorder = UnitOrder(order_id_id=order_id,
                                      product_id=product,
                                      quantity=item["quantity"],
                                      price=product.price + product.tax
                                      )
                unitorder.save()
            unit_orders = UnitOrder.objects.filter(order_id=Order.objects.filter(order_by=self.request.user).values()[0].get("id"))
            order_detail = Order.objects.filter(order_by=self.request.user)
            total_price = round(sum([float(i[0]) for i in list(unit_orders.values_list("price"))]), 2)
            del request.session["cart"]
            return render(
                request,
                template_name="final/final_view.html",
                context={
                    "unit_orders": unit_orders,
                    "total_price": total_price,
                    "order_detail": order_detail
                }
            )
        else:
            try:
                unit_orders = UnitOrder.objects.filter(order_id=Order.objects.filter(order_by=self.request.user).values()[0].get("id"))
            except TypeError:
                return HttpResponseRedirect(reverse_lazy("store_main_view"))

            total_price = round(sum([float(i[0]) for i in list(unit_orders.values_list("price"))]), 2)
            order_detail = Order.objects.filter(order_by=self.request.user)
            return render(
                request,
                template_name="final/checkout_final_view.html",
                context={
                    "unit_orders": unit_orders,
                    "total_price": total_price,
                    "order_detail": order_detail
                }
            )

from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from checkout.forms import AddOrderInfoForm
from store.models import Product
from store.views import CartView


# Create your views here.



class OrderView(CreateView):
    template_name = 'order/order_view.html'
    form_class = AddOrderInfoForm
    success_url = reverse_lazy('store:store_main_view')



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    # def get_form_kwargs(self):
    #     # pass "user" keyword argument with the current user to your form
    #     kwargs = super(MyFormView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs














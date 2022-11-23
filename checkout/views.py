from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from checkout.forms import AddOrderInfoForm
from store.models import Product


# Create your views here.



class OrderView(CreateView):
    template_name = 'order/order_view.html'
    form_class = AddOrderInfoForm

    def get_initial(self):
        return {'order_by': self.request.user.username}







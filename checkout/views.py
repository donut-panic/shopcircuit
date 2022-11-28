from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from checkout.forms import AddOrderInfoForm
from store.models import Order


# Create your views here.



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



class ConfirmView(View):
    def get(self, request):
        return render(
            request,
            template_name="order/confirm.html",
            context={"confirms": Order.objects.all()
            }
        )
















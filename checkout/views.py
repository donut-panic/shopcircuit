from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from checkout.forms import AddOrderInfoForm


# Create your views here.
def fourth_form_submission(request):
    form = AddOrderInfoForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        # save data to DB from session
        try:
            del request.session['cart']
        except KeyError:
            pass
    return HttpResponse("Data has been saved.")


class OrderView(CreateView):
    template_name = 'order/order_view.html'
    form_class = AddOrderInfoForm
    success_url = reverse_lazy('store:store_main_view')
    def post(self, request, *args, **kwargs):
        if self.success_url:
            try:
                del request.session['cart']
            except KeyError:
                pass
        return redirect('/store')




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    # def get_form_kwargs(self):
    #     # pass "user" keyword argument with the current user to your form
    #     kwargs = super(MyFormView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs














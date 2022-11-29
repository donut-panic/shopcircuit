from django.urls import path

from checkout.views import OrderView, ConfirmView, PleaseLoginView, CheckOutView, CheckoutLoginView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order_view'),
    path('confirm/', ConfirmView.as_view(), name='confirm_view'),
    path('confirm/', ConfirmView.as_view(), name='confirm_view'),
    path('please_login/', PleaseLoginView.as_view(), name='p_login'),
    path('login/', CheckoutLoginView.as_view(), name='ch_login'),
    path('final/', CheckOutView.as_view(), name='final'),
]


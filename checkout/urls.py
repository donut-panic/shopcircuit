from django.urls import path

from checkout.views import OrderView, ConfirmView, PleaseLoginView, CheckOutView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order_view'),
    path('confirm/', ConfirmView.as_view(), name='confirm_view'),
    path('confirm/', ConfirmView.as_view(), name='confirm_view'),
    path('login/', PleaseLoginView.as_view(), name='p_login'),
    path('final/', CheckOutView.as_view(), name='final'),
]


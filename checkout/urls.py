from django.urls import path

from checkout.views import OrderView, ConfirmView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order_view'),
    path('confirm/', ConfirmView.as_view(), name='confirm_view'),
]


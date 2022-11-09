from django.template.defaulttags import url
from django.urls import path

from store.views import StoreMainView, StoreCategoryView

app_name = 'store'

urlpatterns = [
    path('', StoreMainView.as_view(), name="store_main_view"),
    path('category/<pk>', StoreCategoryView.as_view(), name="store_main_view"),
]
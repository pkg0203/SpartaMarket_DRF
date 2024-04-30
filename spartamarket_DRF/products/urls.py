from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductsView.as_view(), name="Product"),
    path("<int:product_id>/", ProductsDetailView.as_view(), name="Product_Detail")
]

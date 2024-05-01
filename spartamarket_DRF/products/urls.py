from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductsView.as_view()),
    path("<int:product_id>/", ProductsDetailView.as_view()),
    path("<int:product_id>/like/", ProductLikeView.as_view())
]

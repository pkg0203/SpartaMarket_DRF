from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path("", AccountSignInView.as_view(), name="sign_in"),
    path("<int:user_pk>/", AccountDetailView.as_view(), name="get_profile"),
    path("login/", TokenObtainPairView.as_view(), name="log_in"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

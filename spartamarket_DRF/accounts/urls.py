from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path("", AccountSignInView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("password/", PasswordChangeView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    
    path("<str:username>/", AccountDetailView.as_view()),
    path("<str:username>/follow/", AccountFollowView.as_view()),
]

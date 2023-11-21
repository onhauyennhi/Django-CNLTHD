from django.contrib import admin
from django.urls import path, include
from auth_app.views import login_page, register_page, sign_out
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = "auth_app"

urlpatterns = [
    path('login/', login_page, name ='login'),
    path('register/', register_page, name="register"),
    path("logout/", sign_out, name="logout")
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('restricted/', RestrictedView.as_view(), name="protected_view")
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from django.urls import re_path
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
 
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Normal Authentication.
    # re_path('login',views.login),
    # re_path('signup',views.signup),
    # re_path('test_token',views.test_token),

    #Bearer Authentication
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
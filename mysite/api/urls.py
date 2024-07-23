from django.urls import path
from .import views

from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(),name='blogpost-view-create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(),name='update'),
    #path('blogposts/',views.blog_list),
    #path('blogposts/<int:pk>',views.blog_detail),
    
    #Bearer Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.home,name='home')
    

]
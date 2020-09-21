from django.urls import path
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from django.urls import include, path 
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter 
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
 
router = DefaultRouter() 
router.register('v1/posts', PostViewSet) 
router.register('v1/group', GroupViewSet) 
router.register('v1/follow', FollowViewSet) 
router.register(
    'v1/posts/(?P<id>\d+)/comments', 
    CommentViewSet, basename ='perform_create'
    ) 
 
 
urlpatterns = [
        path(
            'api/v1/token/', 
            TokenObtainPairView.as_view(), 
            name='token_obtain_pair'
        ),
        path(
            'api/v1/token/refresh/', 
            TokenRefreshView.as_view(), 
            name='token_refresh'
        ),
        path('api/', include(router.urls)) 
    ]

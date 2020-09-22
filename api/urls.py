from django.urls import path
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from django.urls import include, path 
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter 
from api.views import PostViewSet, CommentViewSet, GroupList, FollowList
 

router = DefaultRouter() 
router.register('posts', PostViewSet) 
router.register(
    'posts/(?P<id>\d+)/comments', 
    CommentViewSet, basename ='perform_create'
    ) 
 
 
urlpatterns = [
        path(
            'v1/token/', 
            TokenObtainPairView.as_view(), 
            name='token_obtain_pair'
        ),
        path(
            'v1/token/refresh/', 
            TokenRefreshView.as_view(), 
            name='token_refresh'
        ),
        path(
            'v1/group/', 
            GroupList.as_view(), 
            name='group-list'
        ), 
        path(
            'v1/follow/', 
            FollowList.as_view(), 
            name='follow-list'
        ), 
        path('v1/', include(router.urls)),   
    ]

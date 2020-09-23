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
router.register(
    'group', GroupList, basename ='group_list'
    )
router.register(
    'follow', FollowList, basename ='follow_list'
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
        path('v1/', include(router.urls)),   
    ]

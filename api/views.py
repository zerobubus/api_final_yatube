from rest_framework import viewsets, filters, permissions, generics
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response 
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from .models import Post, Comment, Group, Follow
from .permissions import IsOwnerOrReadOnly 
from django_filters.rest_framework import DjangoFilterBackend
 
 
class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly] 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]
 
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user) 
 
 
class CommentViewSet(viewsets.ModelViewSet): 
    serializer_class = CommentSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly] 
     
    def get_queryset(self): 
        return Comment.objects.filter(post=self.kwargs['id']) 
         
    def perform_create(self, serializer):  
        post = get_object_or_404(Post, pk=self.kwargs['id']) 
        serializer.save(author=self.request.user, post=post)  


class GroupList(generics.ListCreateAPIView): 
    queryset = Group.objects.all() 
    serializer_class = GroupSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    

class FollowList(generics.ListCreateAPIView): 
    queryset = Follow.objects.all() 
    serializer_class = FollowSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly] 
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
        
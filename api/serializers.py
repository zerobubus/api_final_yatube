from rest_framework import serializers 
from .models import Post, Comment, Group, Follow
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model
 
 
class PostSerializer(serializers.ModelSerializer): 
    author = serializers.SlugRelatedField( 
        many=False, 
        read_only=True, 
        slug_field='username' 
    ) 

    class Meta: 
        fields = '__all__' 
        model = Post 
 
 
class CommentSerializer(serializers.ModelSerializer): 
    author = serializers.SlugRelatedField( 
        many=False, 
        read_only=True, 
        slug_field='username' 
    ) 
    post = serializers.SlugRelatedField( 
        many=False, 
        read_only=True, 
        slug_field='id' 
    ) 
    class Meta: 
        fields = '__all__' 
        model = Comment 
 

class GroupSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        fields = '__all__' 
        model = Group 


class FollowSerializer(serializers.ModelSerializer): 
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True, 
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField( 
        queryset=get_user_model().objects.all(),
        slug_field='username'
    )
    
    
    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following')
        )
    ]
      
    class Meta: 
        fields = ('user', 'following',)
        model = Follow

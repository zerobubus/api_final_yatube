from django.contrib import admin 
from .models import Post, Comment, Group, Follow
 
 
class PostAdmin(admin.ModelAdmin): 
    list_display = ("id", "text", "pub_date", "author") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = '-пусто-' 


class GroupAdmin(admin.ModelAdmin): 
     
    list_display = ("title",)  
    search_fields = ("title",)  
  

class CommentAdmin(admin.ModelAdmin):  
      
    list_display = ("post", "text", "created", "author", "pk")   
    search_fields = ("post",)   


class FollowAdmin(admin.ModelAdmin): 
     
    list_display = ("user", "following")  
     
 
     
# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin 
admin.site.register(Post, PostAdmin) 
admin.site.register(Comment, CommentAdmin) 
admin.site.register(Group, GroupAdmin) 
admin.site.register(Follow, FollowAdmin) 


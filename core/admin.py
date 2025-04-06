from django.contrib import admin
from .models import FollowerCount, LikePost, Post, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_user', 'bio', 'profile_picture', 'location')
    search_fields = ('user__username', 'bio', 'location')
    list_filter = ('location',)
    ordering = ('user',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at', 'no_of_likes')
    search_fields = ('user', 'caption')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'username')
    search_fields = ('post_id', 'username')
    ordering = ('-post_id',)

@admin.register(FollowerCount)
class FollowerCountAdmin(admin.ModelAdmin):
    list_display = ('follower', 'user')
    search_fields = ('follower', 'user')
    ordering = ('-follower',) 
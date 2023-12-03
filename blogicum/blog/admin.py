from django.contrib import admin

from .models import Location, Category, Post, Comment


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')
    list_display = ('name', 'is_published', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'slug')
    list_filter = ('is_published', 'created_at')
    list_display = ('title', 'description', 'is_published', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text', 'author')
    list_filter = ('pub_date', 'author', 'category', 'location',
                   'is_published', 'created_at')
    list_display = ('title', 'author', 'category',
                    'is_published', 'pub_date', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text', 'author', 'post', 'created_at')
    list_filter = ('text', 'author', 'post', 'created_at')
    list_display = ('text', 'author', 'post', 'created_at')

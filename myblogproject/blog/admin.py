from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Post



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'created_at')
    list_filter = ('blog', 'created_at')
    search_fields = ('title', 'content')

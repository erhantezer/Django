from django.contrib import admin
from blog.models import Category, Post, PostView,Like,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)


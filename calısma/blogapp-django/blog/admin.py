from django.contrib import admin
from blog.models import Category, Post, PostView

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostView)

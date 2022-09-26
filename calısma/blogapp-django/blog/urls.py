from django.urls import path

from blog.views import post_create, post_detail, post_list

app_name = "blog"
urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create, name="create"),
    path("<slug:slug>/", post_detail, name="detail"),
]




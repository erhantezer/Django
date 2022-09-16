from .views import add

from django.urls import path

from todo.views import home

urlpatterns = [
    path("", home, name="home"),
    path("add/", add, name="add"),
]

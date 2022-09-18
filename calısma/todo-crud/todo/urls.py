from .views import add, update
from django.urls import path
from todo.views import home

urlpatterns = [
    path("", home, name="home"),
    path("add/", add, name="add"),
    path("update/<int:id>", update, name="update")
]

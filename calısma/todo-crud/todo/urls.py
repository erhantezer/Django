from .views import add, delete, update
from django.urls import path
from todo.views import home

urlpatterns = [
    path("", home, name="home"),
    path("add/", add, name="add"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
]

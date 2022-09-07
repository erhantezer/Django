
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import(
    home,
    register,
    special,
    ) 

urlpatterns = [
   
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("special/", special, name="special"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),
    name='change-password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'), name='reset-password'),
]
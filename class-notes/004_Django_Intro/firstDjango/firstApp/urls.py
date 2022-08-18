
from django.urls import path

from firstApp.views import firstApp
urlpatterns = [
    
    path('', firstApp)
]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from student.views import index, student_page


urlpatterns = [
    
    path("", student_page, name="student")
     
]

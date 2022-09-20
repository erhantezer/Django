from django.urls import path
from .views import ( 
    ##! FBV URLS
    # student_api,
    # student_api_get_update_delete, path_api,
    # student_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_update_partial,
    # student_delete
    
    StudentDetail,
    StudentURD,
    # StudentList,
    home,
    StudentListCreate,
    )




urlpatterns = [
    path('', home),
    # path("student/", StudentList.as_view()), #? APIView
    # path("student/<int:pk>",StudentDetail.as_view()), #? APIView
    path("student/",StudentListCreate.as_view()), #? Generic APIView
    path("student/<int:pk>",StudentURD.as_view()), #? Generic APIView
    
]
##! FBV URLS
    
    # path('student/', student_api),
    # path('student/<int:pk>/', student_api_get_update_delete, name="detail"),
    # path('path/', path_api),
    # path('student_list/', student_list, name='student_list'),
    # path('student_create/', student_create, name='student_create'),
    # path('student_detail/<int:pk>/', student_detail, name='student_detail'),
    # path('student_update/<int:pk>/', student_update, name='student_update'),
    # path('student_update_partial/<int:pk>/',
    #      student_update_partial, name='student_update_partial'),
    # path('student_delete/<int:pk>/', student_delete, name='student_delete'),
    
   
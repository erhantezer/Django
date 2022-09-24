from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Todo, Category
from .serializers import TodoSerializers, CategorySerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

#? viewset Apı oluşturma kullandık routeri unutma
#? crud  işlemlerinin hepsine izin verir
class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

#? concrate Apı Views  oluşturma (mixin ile generic birleşimi) get ve post işlemi yapar   
class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
#? concrate Views update delete işlemi sağlıyor    
class CategoryUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field= "id"
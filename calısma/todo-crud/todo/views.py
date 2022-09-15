from .forms import TodoForm
from todo.models import Todo
from django.shortcuts import render

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    
    context = {
        "todos":todos,
        "form":form,
    }
    return render(request, "todo/home.html", context)
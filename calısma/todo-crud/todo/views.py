
from django.contrib import messages
from .forms import TodoForm
from todo.models import Todo
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    
    context = {
        "todos":todos,
        "form":form,
    }
    return render(request, "todo/home.html", context)

def add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Todo created successfully")
        return redirect("home")
    context = {
        "form":form
    }
    return render(request, "todo/todo_add.html", context)
    
def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    
    # if request.method == "POST":
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("home")
        
    context = {
        "todo":todo,
        "form":form,
    }
    return render(request, "todo/todo_update.html", context)
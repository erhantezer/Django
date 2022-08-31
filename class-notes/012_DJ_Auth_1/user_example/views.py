from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")


def register(request):
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        # username = form.cleaned_data.get("username")
        # password = form.cleaned_data.get("password1")
        # user = authenticate(username=username, password=password)
        # login(request, user)
        return redirect("home")
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)




def password_change(request):
    if request.method == 'POST':
        
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/password_change.html", context)
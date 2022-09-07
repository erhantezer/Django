from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "user/home.html")


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # buraya kadar olan işlemler register olmya yeterli
        #buradan sonra ki işlemler register ileirlikte login olmasını istersek
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request,user)
        #login otomatik olacağı için artık redirect içine home yazıyoruz 
        # return redirect("login")
        return redirect("home")
    context = {
        "form":form
    }
    return render(request, "registration/register.html",context)


@login_required
def special(request):
    return render(request,"user/special.html")
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required
from .forms import  UserRegistrationForm 
from django.contrib.auth.hashers import make_password , check_password
from .models import user_model



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.password = make_password(request.POST["password"])
            new_user.save()
            return render(request, 'register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = user_model.objects.get(username=username)
        if u is None:
            context = {"error":"Invalid username or password."}
            return render(request,"registration/login.html",context)
        elif check_password(password,u.password) and u is not None:
            if u.is_active:
                login(request,u)
                return redirect('home')
        else:
            return render(request,"registration/login.html")
    return render(request,"registration/login.html")




@login_required
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

@login_required
def calculator(request):
    return render(request,'calculator.html')

@login_required
def ttt(request):
    return render(request,'ttt.html')

@login_required
def tdl(request):
    return render(request,'tdl.html')

@login_required
def rps(request):
    return render(request,'rps.html')
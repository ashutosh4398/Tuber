from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)
            messages.success(request, message="logged in successfully")
            return redirect("dashboard")
        messages.error(request,"invalid credentials")
        return redirect('login')
    return render(request,"accounts/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,message="username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,message="email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email = email,
                    password = password
                )

                user.save()

                messages.success(request,message="Account created successfully.")
                return redirect('login')
        else:
            messages.error(request,message="Passwords do not match")
            return redirect('register')

    return render(request,"accounts/register.html")

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
def dashboard(request):
    return render(request,"accounts/dashboard.html")


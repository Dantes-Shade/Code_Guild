from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

def login_user(request):
    username = request.POST.get('InputUsername')
    password = request.POST.get('InputPassword1')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'todos/list.html' )
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

User = get_user_model()
# creates new user
def register_new_user(request):
    if request.method == 'POST':
        new_user = User(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        username = request.POST['username'],
        email = request.POST['email'],
        )

        password = request.POST['password']
        new_user.set_password(password)
        new_user.save()

        return redirect('list')
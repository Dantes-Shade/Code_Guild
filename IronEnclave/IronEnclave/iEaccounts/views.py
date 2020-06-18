from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate
from iEaccounts.models import Users, Profiles
from iEgraph.models import Graph

# Create your views here.

def login_user(request):
    username = request.POST.get('InputUsername')
    password = request.POST.get('InputPassword1')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home_page.html' )
    else:
        return render(request, 'iEaccounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('ironenclave:home/')

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

        return redirect('iEcommunity:home_page')
    else:
        return render(request, 'iEaccounts/register.html')

def user_profile(request):
    prof_mod = Profiles.objects.filter(user = request.user)
    graph_mod = Graph.objects.filter(user = request.user)

    context = {
        'prof_mod': prof_mod,
        'graph_mod': graph_mod,
    }

    return render(request, 'iEaccounts/profile.html', context)

# POST-Updating profile
def update_profile(request):
    if request.method == 'POST':
    
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        age = request.POST['age']
        profile_img = request.POST['profile_img']
        bio = request.POST['bio']
        gender = request.POST['gender']
        weight_class = request.POST['weight_class']
    
        return redirect('profile')

    else:
        return render(request, 'iEaccounts/update_profile.html')

def update_graph(request):
    if request.method == 'POST':

        weight = request.POST['weight']
        lift = request.POST['lift']

        return redirect('profile')


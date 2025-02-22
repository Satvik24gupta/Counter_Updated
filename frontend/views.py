from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from .models import User, Counter
import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    return redirect('login')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:    
        return render(request, 'login.html')
    
def home(request):
    if(request.user.is_authenticated):
        return render(request, 'home.html')
    else:
        messages.info(request, 'Please Login First')
        return redirect('login')

def logout(request):
    print("Log Out ho gaya")
    auth_logout(request)
    return redirect('login')

def add_counter(request):
    # if request.method == 'POST':
    print(request.user.id)
    # user = User.objects.filter(id=request.user.id)
    user = request.user.id
    print("USer: ", user)
    # print("user: ", list(user.values()))
    counter = Counter.objects.create(user_id = user)

    # counter = Counter.objects.create(user_id =request.user.id)
    counter.save()
    counter = Counter.objects.all()
    # counter = Counter.objects.all()
    counter_data = list(counter.values())
    return JsonResponse(counter_data, safe=False)
    # return render(request, 'home.html', {'counter': counter})
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
    print(request.user.id)
    user = request.user.id
    print("USer: ", user)
    counter = Counter.objects.create(user_id = user)
    counter.save()
    counter = Counter.objects.all()
    counter_data = list(counter.values())
    return JsonResponse(counter_data, safe=False)

def increment_counter(request):
    print(request.user.id)
    user = request.user.id
    request_data = json.loads(request.body)
    print("Id from Post request: ", request_data.get("id"))
    counter_id = request_data.get("id")
    counter = Counter.objects.get(user_id=user, id=counter_id)
    counter.value += 1
    counter.save()
    counter_data = Counter.objects.all().order_by('id')
    counter_data = list(counter_data.values())
    return JsonResponse(counter_data, safe=False)

def decrement_counter(request):
    print(request.user.id)
    user = request.user.id
    request_data = json.loads(request.body)
    counter_id = request_data.get("id")
    counter = Counter.objects.get(user_id=user, id=counter_id)
    counter.value -= 1
    counter.save()
    counter_data = Counter.objects.all().order_by('id')
    counter_data = list(counter_data.values())
    return JsonResponse(counter_data, safe=False)

def reset_counter(request):
    print(request.user.id)
    user = request.user.id
    request_data = json.loads(request.body)
    counter_id = request_data.get("id")
    counter = Counter.objects.get(user_id=user, id=counter_id)
    counter.value = 0
    counter.save()
    counter_data = Counter.objects.all().order_by('id')
    counter_data = list(counter_data.values())
    return JsonResponse(counter_data, safe=False)

def delete_counter(request):
    print(request.user.id)
    user = request.user.id
    request_data = json.loads(request.body)
    counter_id = request_data.get("id")
    counter = Counter.objects.get(user_id=user, id=counter_id)
    counter.delete()
    counter_data = Counter.objects.all().order_by('id')
    counter_data = list(counter_data.values())
    return JsonResponse(counter_data, safe=False)

def reset_all_counter_value(request):
    print(request.user.id)
    user = request.user.id
    Counter.objects.filter(user_id=user).update(value=0)
    counter_data = Counter.objects.all().order_by('id')
    counter_data = list(counter_data.values())
    return JsonResponse(counter_data, safe=False)

def get_counters(request):
    user = request.user.id
    counters = Counter.objects.filter(user_id=user).order_by('id')
    counter_data = list(counters.values())
    return JsonResponse(counter_data, safe=False)
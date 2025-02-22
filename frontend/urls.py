from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('add_counter', views.add_counter, name='add_counter'),
    # path('register/', views.register, name='register'),
]
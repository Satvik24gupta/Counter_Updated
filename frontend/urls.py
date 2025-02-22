from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('add_counter', views.add_counter, name='add_counter'),
    path('increment_counter', views.increment_counter, name='increment_counter'),
    path('decrement_counter', views.decrement_counter, name='decrement_counter'),
    path('reset_counter', views.reset_counter, name='reset_counter'),
    path('delete_counter', views.delete_counter, name='delete_counter'),
    path('reset_all_counter_value', views.reset_all_counter_value, name='reset_all_counter_value'),
    path('get_counters', views.get_counters, name='get_counters'),
    # path('register/', views.register, name='register'),
]
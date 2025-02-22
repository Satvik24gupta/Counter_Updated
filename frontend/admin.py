from django.contrib import admin
from .models import User, Counter

# Register your models here.
admin.site.register(User)
admin.site.register(Counter)
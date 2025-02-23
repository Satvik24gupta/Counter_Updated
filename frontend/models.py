from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     # Basic User model with necessary fields
#     username = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=255, blank=True)
#     last_name = models.CharField(max_length=255, blank=True)
    
#     def _str(self):
#         return self.username

class Counter(models.Model):
    # Each counter has a unique counter_id, a counter value, and a foreign key to User
    counter_name = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(default=0)  # Starting value for the counter
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='counters',null=True)

    def __str_(self):
        return f"Counter {self.counter_id} for {self.user.username} with value {self.value}"
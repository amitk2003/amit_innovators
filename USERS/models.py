from django.db import models
# user/models.py
from django.contrib.auth.models import User

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"

class AdminLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin.username} - {self.action} - {self.timestamp}"


# Create your models here.
class Event(models.Model):
    date = models.DateField()
    event_category = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    food_type = models.CharField(max_length=100)
    advance_payment_policy = models.TextField()



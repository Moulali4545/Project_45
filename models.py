from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.PositiveSmallIntegerField(max_length=10)

    def __str__(self):
       return self.first_name

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=200)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)        

    def __str__(self):
       return self.user.username    
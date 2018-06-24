from django.db import models

# Create your models here.
#lesson 127
class User (models.Model):
    name=models.CharField(max_length=264, unique=True)
    surname=models.CharField(max_length=264, unique=True)
    email=models.EmailField(max_length=264, unique=True)
    age=models.IntegerField(default=0)
    password=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class UserAge(models.Model):
    user_age=models.IntegerField(default=0)
    user_name=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_age)

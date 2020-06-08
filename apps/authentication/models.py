from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Profile(models.Model):
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='user_avatars/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
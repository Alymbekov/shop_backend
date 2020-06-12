from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


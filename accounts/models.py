from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    face_auth = models.BooleanField(default=False)
    voice_auth = models.BooleanField(default=False)
    gesture_auth = models.BooleanField(default=False)

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
    ("ADMIN", "Admin"),
    ("DOCTOR", "Doctor"),
    ("RECEPTIONIST", "Receptionist"),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"
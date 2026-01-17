from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE","Female"),
        ("OTHER","Other"),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
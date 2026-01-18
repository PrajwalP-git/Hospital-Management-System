from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class MedicalRecord(models.Model):
    doctor = models.ForeignKey(
        "doctors.Doctor",
        on_delete=models.CASCADE,
        related_name="medical_records"
    )

    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.CASCADE,
        related_name="medical_records"
    )

    diagnosis = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.diagnosis.strip():
            raise ValidationError("diagnosis cannot be empty.")

    def __str__(self):
        return f"{self.patient} - {self.diagnosis[:30]}"
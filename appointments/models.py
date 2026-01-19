from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES = (
        ("SCHEDULED","Scheduled"),
        ("COMPLETED","Completed"),
        ("CANCELLED","Cancelled"),
    )

    doctor = models.ForeignKey(
        "doctors.Doctor",
        on_delete=models.CASCADE,
        related_name='Appointments'
    )

    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.CASCADE,
        related_name='Appointments'
    )

    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices = STATUS_CHOICES,
        default = "SCHEDULED"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):          #end time must be after start time
        if self.start_time > self.end_time:
            raise ValidationError("End time must be after start time.")

        #ignore cancelled appointments
        qs = Appointment.objects.filter(
            doctor=self.doctor,
            status = "SCHEDULED",
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )

        def clean(self):
            if self.status !="Scheduled":
                return
            if self.status == "Completed":
                return
        #doctor conflict
        qs = Appointment.objects.filter(
            doctor=self.doctor,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )

        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Doctor already has an appointment in this time")

        def clean(self):
            if self.status !="Scheduled":
                return
        #patient conflict
        qs = Appointment.objects.filter(
            patient=self.patient,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )

        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Patient already has an appointment in this time")

        def __str__(self):
            return f"{self.patient} -> {self.doctor} ({self.appointment_date})"
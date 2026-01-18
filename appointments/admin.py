from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "appointment_date",
        "start_time",
        "end_time",
        "doctor",
        "patient",
        "status",
    )
    list_filter = ("status","appointment_date", "doctor")
    search_fields = ("patient_name","doctor_user_username")

    def save_model(self, request, obj, form, change):
        obj.full_clean() #enforces conflict rules
        super().save_model(request,obj,form,change)
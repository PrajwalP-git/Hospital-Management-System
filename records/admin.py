from django.contrib import admin
from .models import MedicalRecord

@admin.register(MedicalRecord)
# Register your models here.
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("created_at","patient","doctor","diagnosis")
    list_filter = ("doctor","created_at")
    search_fields = ("patient__name","diagnosis")

    def save_model(self, request, obj, form, change):
        obj.full_clean()
        super().save_model(request,obj,form,change)
from django.contrib import admin
from .models import Doctor, Department

@admin.register(Department)
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user","department","specialization", "is_active")
    list_filter = ("department", "is_active")
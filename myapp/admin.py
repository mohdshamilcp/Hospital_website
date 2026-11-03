from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "department", "appointment_date", "status")
    list_filter = ("status", "department")
    list_editable = ("status",)


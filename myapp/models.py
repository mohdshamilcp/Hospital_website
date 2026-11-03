from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Appointment(models.Model):
    DEPARTMENT_CHOICES = [("general-medicine", "General Medicine"),
        ("cardiology", "Cardiology"),
        ("pediatrics", "Pediatrics"),
        ("orthopedics", "Orthopedics"),
        ("neurology", "Neurology"),
        ("other", "Other"),]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),]

    patient_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    department = models.CharField(max_length=40, choices=DEPARTMENT_CHOICES)
    appointment_date = models.DateField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending",)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date", "created_at"]

    def __str__(self):
        return "{self.patient_name} - {self.appointment_date}"


class Review(models.Model):
    reviewer_name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return "{self.reviewer_name} - {self.rating}/5"

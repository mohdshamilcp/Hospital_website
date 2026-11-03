from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.dateparse import parse_date

from .models import Appointment, Review


def index(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "review":
            reviewer_name = request.POST.get("reviewer_name", "").strip()
            comment = request.POST.get("comment", "").strip()

            try:
                rating = int(request.POST.get("rating", ""))
            except (TypeError, ValueError):
                rating = 0

            if reviewer_name and comment and 1 <= rating <= 5:
                Review.objects.create(reviewer_name=reviewer_name,rating=rating,comment=comment,)
                messages.success(request, "Thank you for reviewing the hospital.")
            else:
                messages.error(request,"Enter your name, a 1–5 star rating, and a review.",)

            return redirect("index")

        if form_type == "appointment":
            patient_name = request.POST.get("patient_name", "").strip()
            phone = request.POST.get("phone", "").strip()
            department = request.POST.get("department", "")
            appointment_date = parse_date\

            (request.POST.get("appointment_date", ""))

            message = request.POST.get("message", "").strip()
            valid_departments = dict(Appointment.DEPARTMENT_CHOICES)

            valid_request = (patient_name and phone and department in valid_departments and appointment_date and appointment_date >= timezone.localdate())

            if valid_request:
                Appointment.objects.create(patient_name=patient_name,phone=phone,department=department,appointment_date=appointment_date,message=message,)
                messages.success(request, "Your appointment request has been received.",)
            else:
                messages.error(request,"Check your details and choose a valid appointment date.",)

            return redirect("index")

    reviews = Review.objects.all()[:6]
    return render(request, "index.html", {"reviews": reviews})
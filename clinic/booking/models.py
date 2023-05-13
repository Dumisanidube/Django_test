from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Doctor ", "Doctor "),
    ("NURSING CARE", "NURSING CARE"),
    ("SOCIAL WORKER", "SOCIAL WORKER"),
    ("C.E.O", "C.E.O"),
    )
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM ","10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("13 PM", "13 PM"),
    ("14 PM", "14 PM"),
    ("15 PM", "15 PM"),
    ("16 PM", "16 PM"),
    ("17 PM", "17 PM"),
    
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
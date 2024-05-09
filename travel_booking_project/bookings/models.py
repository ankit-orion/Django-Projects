# bookings/models.py
from django.db import models

class Booking(models.Model):
    DESTINATION_CHOICES = (
        ('Paris', 'Paris'),
        ('New York', 'New York'),
        ('Tokyo', 'Tokyo'),
        ('London', 'London'),
        ('Sydney', 'Sydney'),
        # Add more destinations as needed
    )

    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    adults = models.IntegerField(default=1)  # Number of adult travelers
    children = models.IntegerField(default=0)  # Number of children travelers
    special_requests = models.TextField(blank=True)  # Special requests or notes

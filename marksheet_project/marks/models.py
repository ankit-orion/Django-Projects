# marks/models.py
from django.db import models

class Mark(models.Model):
    STUDENT_CHOICES = [
        ('John Doe', 'John Doe'),
        ('Alice Smith', 'Alice Smith'),
        ('Bob Johnson', 'Bob Johnson'),
        # Add more students as needed
    ]
    SUBJECT_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('History', 'History'),
        # Add more subjects as needed
    ]

    student_name = models.CharField(max_length=100, choices=STUDENT_CHOICES)
    subject_name = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.subject_name}: {self.marks}"

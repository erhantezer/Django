from django.db import models

# Create your models here.
status_choices = [
    ("completed"),
    ("pending"),
    ("In-Progress")
]

priority_choices = [
   ("1️⃣"),
   ("2️⃣"),
   ("3️⃣")
]

class Todo(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=status_choices)
    priority = models.CharField(max_length=2, choices=priority_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
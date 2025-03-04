from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

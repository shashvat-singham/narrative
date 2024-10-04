from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    state = models.CharField(max_length=2)  # Two-letter state code

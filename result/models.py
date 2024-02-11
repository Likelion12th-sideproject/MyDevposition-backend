from django.db import models

# Create your models here.

class TestResult(models.Model):
    result = models.CharField(max_length=10, choices=(
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('planning', 'Planning'),
    ))

    def __str__(self):
        return self.result
from django.db import models

# Create your models here.

class User(models.Model):
    GRADE_CHOICES = [
        (1, '1학년'),
        (2, '2학년'),
        (3, '3학년'),
        (4, '4학년'),
        (5, '기타'),
    ]

    RESULT_CHOICES = [
        ('frontend', '프론트엔드'),
        ('backend', '백엔드'),
        ('fullstack', '풀스택'),
        ('plan/design', '기획/디자인'),
    ]

    grade = models.IntegerField(verbose_name='학년', choices=GRADE_CHOICES)
    result = models.CharField(verbose_name='결과', max_length=15, choices=RESULT_CHOICES)
from django.db import models
from user.models import User
# Create your models here.
class Time(models.Model):
    time = models.CharField(max_length=100)

class Slot(models.Model):
    teacher 			= models.ForeignKey(User, limit_choices_to={'is_teacher': True}, related_name="teacher", on_delete=models.CASCADE, null=True)
    date                = models.DateField()
    time                = models.ManyToManyField(Time)
    student             = models.ForeignKey(User, limit_choices_to={'is_student': True}, related_name="student", on_delete=models.CASCADE, null=True)
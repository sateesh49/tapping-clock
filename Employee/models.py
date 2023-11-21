from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=100)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateTimeField(null=True)
    #empcode = models.CharField(null=True)

    def __str__(self):
        return self.user.username

class Holiday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    holiday_name = models.CharField(max_length=255)
    is_holiday = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.holiday_name}"




class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.title






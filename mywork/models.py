from django.db import models

# Create your models here.
class work_history(models.Model):
    company = models.CharField(max_length=100)
    start_work = models.DateField(auto_now=False, auto_now_add=False)
    end_work = models.DateField(auto_now=False, auto_now_add=False)
    job_position=models.CharField(max_length=200)
    job_description = models.TextField()
    
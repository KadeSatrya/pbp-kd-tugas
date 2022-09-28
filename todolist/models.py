from tkinter import Button
from django.db import models
from django.contrib.auth.models import User

# Model Task
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True) # auto_now_add akan mengatur date sebagai tanggal pembuatan object Task yang baru
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
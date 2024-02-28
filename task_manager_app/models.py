# task_manager_app/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'task_manager_app'  # Add the app_label attribute

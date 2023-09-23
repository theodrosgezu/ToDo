from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = model.CharField(max_length=100)
    details = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
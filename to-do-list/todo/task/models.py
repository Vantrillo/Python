from django.db import models

# Create your models here.
class Task(models.Model):
    class Priority(models.IntegerChoices):
        Low = 1
        MEDIUM = 2
        HIGH = 3
        URGENT = 4

    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=200, blank=True, default='')
    status = models.BooleanField(default=False)
    priority = models.IntegerField(choices=Priority.choices, default = 1)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
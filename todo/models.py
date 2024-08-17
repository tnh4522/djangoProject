from django.db import models
from django.utils import timezone


class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.text}: due {self.due_date}"


class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

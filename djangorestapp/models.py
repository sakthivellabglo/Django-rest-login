from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.CharField(max_length=180)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    description = models.TextField(blank=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return " {} {} {} {} ".format(self.title, self.image, self.price, self.stock)

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




class Product(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    description = models.TextField(blank=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return " {} {} {} {} ".format(self.title, self.image, self.price, self.stock)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        ordering = ['created']

class Doctor(models.Model):

    id= models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.id

class Patient(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True)
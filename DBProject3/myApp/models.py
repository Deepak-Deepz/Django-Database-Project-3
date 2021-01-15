from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    mail = models.EmailField(max_length = 50)
    ph = models.CharField(max_length = 10)
    def __str__(self):
        return self.name

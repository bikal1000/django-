from django.db import models

# Create your models here.
class Form(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField(max_length=150)


    def __str__(self):
        return self.firstname
    
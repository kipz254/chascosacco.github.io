from django.db import models

# Create your models here.
class Member(models.Model):
    image = models.ImageField(upload_to = 'Member_Pimages/',blank=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    zone = models.CharField(max_length=25)

    def __str__(self):
          return self.name

class Management(models.Model):
    image = models.ImageField(upload_to = 'Management_Pimages/',blank=True)
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)

    def __str__(self):
        return self.name

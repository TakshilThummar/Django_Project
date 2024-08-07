from django.db import models

# Create your models here.

class Contact (models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    class Meta:
        db_table = "Portfolio_Website"

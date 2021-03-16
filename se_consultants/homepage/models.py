from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact_no = models.IntegerField(default=0)
    message = models.TextField()
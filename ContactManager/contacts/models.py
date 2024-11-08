from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    notes=models.TextField()
    profile_picture=models.ImageField(upload_to='profile_pices/',blank=True,null=True)
    def __str__(self):
        return self.name
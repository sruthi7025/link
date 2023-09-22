from django.db import models

class  Address(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    def __str__(self):
        return self.name


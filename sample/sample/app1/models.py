from django.db import models

# Create your models here.
class table(models.Model):
    name=models.TextField()
    country=models.TextField()
    city=models.TextField()
    salary=models.IntegerField()
class table1(models.Model):
    content=models.TextField()
class table2(models.Model):
    number=models.IntegerField()
    name=models.TextField()
    salary=models.IntegerField()
    country=models.TextField()

from django.db import models
from django.urls import reverse

# Create your models here.
class PersonApp(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=50)
    city=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('personinfo:index')

    def __str__(self):
        return "  "+self.fname+"  "+self.lname+" "


class Department(models.Model):
    pid = models.ForeignKey(PersonApp,on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_name,self.pid





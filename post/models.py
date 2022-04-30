from statistics import mode
from django.db import models #python file that contains model class and other classes that have specific purposes

class Post(models.Model):
    title = models.CharField(max_length=256) #defining our first column
    body = models.TextField() #defining our second column

    def __str__(self):
        return self.title
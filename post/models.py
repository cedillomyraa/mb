
from django.db import models #python file that contains model class and other classes that have specific purposes
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256) #defining our first column
    body = models.TextField() #defining our second column

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
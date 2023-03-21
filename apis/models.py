import datetime

from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, models.CASCADE)
    photo = models.ImageField(upload_to='images', default='default.png')
    createdAt = models.DateTimeField(default=datetime.datetime.now)
    desc = models.TextField(default='description')

    def __str__(self):
        return self.title + " " + self.category.name


class RecentWork(models.Model):
    photo = models.ImageField(upload_to='images', default='default.png')

    def __str__(self):
        return str(self.id)


class ImageGallery(models.Model):
    photo = models.ImageField(upload_to='images', default='default.png')

    def __str__(self):
        return str(self.id)


class Aboutme(models.Model):
    photo = models.ImageField(upload_to='images', default='default.png')
    desc = models.TextField(default='description')

    def __str__(self):
        return str(self.id)

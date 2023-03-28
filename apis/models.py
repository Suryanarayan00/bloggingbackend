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
    headerText1 = models.CharField(default="Hi there!,\n I am Nilesh", max_length=100)
    headerText2 = models.CharField(default="Welcomes to my blogpost", max_length=100)
    headerImage = models.ImageField(default='boat.png', upload_to='images' )
    githubLink = models.CharField(default='google.com', max_length=200)
    instagramLink = models.CharField(default='google.com', max_length=200)
    linkedInLink = models.CharField(default='google.com', max_length=200)
    footerHeader=models.CharField(default='Nilesh Chandrakant', max_length=200)
    footerSubheader = models.CharField(default='I can do anything, nothing is impossible and thats it', max_length=300)
    phoneNumber = models.CharField(default='', max_length=13)
    email = models.CharField(default='', max_length=50)

    def __str__(self):
        return str(self.id)

from django.contrib import admin
from .models import BlogPost, Category, RecentWork, ImageGallery, Aboutme

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(RecentWork)
admin.site.register(ImageGallery)
admin.site.register(Aboutme)
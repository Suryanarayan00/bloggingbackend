from rest_framework import serializers
from .models import Category, BlogPost, RecentWork, ImageGallery, Aboutme


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecentWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentWork
        fields = '__all__'


class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = '__all__'


class AboutmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutme
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

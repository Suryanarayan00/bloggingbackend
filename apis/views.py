from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import BlogPost, Category, ImageGallery, RecentWork, Aboutme
from .serializers import BlogPostSerializer, CategorySerializer, RecentWorkSerializer, AboutmeSerializer, \
    ImageGallerySerializer


# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogPostViewset(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category__name']
    search_fields = ['category__name']
    ordering_fields = ['category__name']
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class RecentWorkViewset(viewsets.ModelViewSet):
    serializer_class = RecentWorkSerializer
    queryset = RecentWork.objects.all()


class ImageGalleryViewset(viewsets.ModelViewSet):
    serializer_class = ImageGallerySerializer
    queryset = ImageGallery.objects.all()


class AboutmeViewset(viewsets.ModelViewSet):
    serializer_class = AboutmeSerializer
    queryset = Aboutme.objects.all()

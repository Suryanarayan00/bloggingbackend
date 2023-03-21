from django.urls import path, include

from .views import CategoryViewset, BlogPostViewset, AboutmeViewset, ImageGalleryViewset, RecentWorkViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewset, basename='catgegory')
router.register('blog', BlogPostViewset, basename='blog')
router.register('aboutme', AboutmeViewset, basename='aboutme')
router.register('imageGallery', ImageGalleryViewset, basename='imageGallery')
router.register('recentWork', RecentWorkViewset, basename='recentWork')


urlpatterns = [
    path('apis/', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserActivityLogViewSet

router = DefaultRouter()
router.register(r'logs', UserActivityLogViewSet, basename='activity-log')

urlpatterns = [
    path('', include(router.urls)),
]

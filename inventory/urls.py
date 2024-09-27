from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet  # Import the ItemViewSet from views.py

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='items')  # Register ItemViewSet with the router

urlpatterns = [
    path('', include(router.urls)),  # Include the automatically generated router URLs
]

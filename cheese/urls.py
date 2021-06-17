from django.urls import path, include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from cheeses import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cheeses', views.CheeseViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'rating', views.RatingViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

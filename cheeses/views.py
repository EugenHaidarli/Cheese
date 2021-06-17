from cheeses.models import Cheese, Review, Rating
from rest_framework import serializers, viewsets
from .serializers import CheeseSerializer, UserSerializer, ReviewSerializer, RatingSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.contrib.auth.models import User

class CheeseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Cheese.objects.all()
    serializer_class = CheeseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Review viewset automagically provides list, create, retrieve, update and destroy actions
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RatingViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

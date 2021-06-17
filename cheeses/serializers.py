from rest_framework import serializers
from .models import Cheese, Review, Rating
from django.contrib.auth.models import User

class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cheese
        fields = ['url', 'id', 'name', 'description', 'firmness', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    cheeses = serializers.HyperlinkedRelatedField(many=True, view_name='cheese-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'cheeses']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ['url', 'id', 'cheese', 'content', 'score', 'owner']

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rating
        fields = ['url', 'id', 'review', 'vote', 'owner']

from rest_framework import serializers
from .models import Cheese, Review, Rating
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    cheeses = serializers.HyperlinkedRelatedField(many=True, view_name='cheese-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'cheeses', 'reviews', 'ratings']

class RatingSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['url', 'id', 'review', 'vote', 'owner']

class Upvotes(serializers.RelatedField):
    def to_representation(self, value):
        return value.vote

class ReviewSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    # ratings = RatingSerializer(many=True, read_only=True)
    ratings = Upvotes(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['url', 'id', 'cheese', 'content', 'score', 'owner', 'ratings']


class CheeseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Cheese
        fields = ['url', 'id', 'name', 'description', 'firmness', 'owner', 'reviews']

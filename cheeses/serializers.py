from re import A
from rest_framework import serializers
from .models import Cheese, Review, Rating
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # cheeses = serializers.HyperlinkedRelatedField(many=True, view_name='cheese-detail', read_only=True)
    cheeses = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_cheeses(self, cheese):
        return cheese.cheeses.count()

    def get_reviews(self, review):
        return review.reviews.count()

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'cheeses', 'reviews']

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
    rating_score = serializers.SerializerMethodField()

    def get_rating_score(self, review):
        return {
            "upvotes": review.ratings.filter(vote='1').count(), 
            "downvotes": review.ratings.filter(vote='-1').count()
        }

    class Meta:
        model = Review
        fields = ['url', 'id', 'cheese', 'content', 'score', 'owner', 'rating_score']


class CheeseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Cheese
        fields = ['url', 'id', 'name', 'description', 'firmness', 'owner', 'reviews']

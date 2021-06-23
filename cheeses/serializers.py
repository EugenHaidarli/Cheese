from rest_framework import serializers
from .models import Cheese, Review, Rating
from django.contrib.auth.models import User

class UserCheeseSerializer(serializers.ModelSerializer):
    cheese_count = serializers.SerializerMethodField()

    def get_cheese_count(self, cheese):
        return cheese.cheeses.count()

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'cheese_count']


class UserReviewSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()

    def get_review_count(self, cheese):
        return cheese.reviews.count()

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'review_count']

class RatingSerializer(serializers.ModelSerializer):
    owner = UserReviewSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['url', 'id', 'review', 'vote', 'owner']

class Upvotes(serializers.RelatedField):
    def to_representation(self, value):
        return value.vote

class ReviewSerializer(serializers.ModelSerializer):
    owner = UserReviewSerializer(read_only=True)
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
    owner = UserCheeseSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Cheese
        fields = ['url', 'id', 'name', 'description', 'firmness', 'owner', 'reviews']

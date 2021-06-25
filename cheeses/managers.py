from django.db import models
from django.db.models import Count

class CheeseQuerySet(models.QuerySet):
    def get_cheeses_for_users(self, users):
        return self.filter(owner__in=users)
    
    def get_top_cheese(self, size=5):
        return self.all().annotate(reviews_count=Count('reviews')).order_by('-reviews_count')[:size]

class CheeseManager(models.Manager):
    def get_queryset(self):
        return CheeseQuerySet(self.model, using=self._db)

    def get_cheeses_for_users(self, users):
        return self.get_queryset().get_cheeses_for_users(users)

    def get_top_cheese(self, size):
        return self.get_queryset().get_top_cheese(size)

class ReviewQuerySet(models.QuerySet):
    def get_reviews_for_score(self, score):
        return self.filter(score=score)

    def get_reviews_by_content(self, string):
        return self.filter(content__icontains=string)

    def get_top_review(self, cheese):
        return self.filter(cheese__name=cheese).annotate(ratings_count=Count('ratings__vote' == 1)).order_by('-ratings_count')[:1]

class ReviewManager(models.Manager):
    def get_queryset(self):
        return ReviewQuerySet(self.model, using=self._db)

    def get_reviews_for_score(self, score):
        return self.get_queryset().get_reviews_for_score(score)

    def get_reviews_by_content(self, string):
        return self.get_queryset().get_reviews_by_content(string)

    def get_top_review(self, cheese):
        return self.get_queryset().get_top_review(cheese)

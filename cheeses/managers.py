from django.db import models

class CheeseQuerySet(models.QuerySet):
    def get_users_cheese(self, username):
        return self.filter(owner__username=username)
    
    def get_top_cheese(self, size):
        return self.filter(reviews__gt=size)

    def test(self):
        return self.filter(reviews__cheese=2)

class CheeseManager(models.Manager):
    def get_queryset(self):
        return CheeseQuerySet(self.model, using=self._db)

    def get_users_cheese(self, username):
        return self.get_queryset().get_users_cheese(username)

    def get_top_cheese(self, size):
        return self.get_queryset().get_top_cheese(size)

    def test(self):
        return self.get_queryset().test()

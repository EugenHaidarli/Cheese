from django.db import models

class Cheese(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', null=True, related_name='cheeses', on_delete=models.CASCADE)

    class Firmness(models.TextChoices): 
        UNSPECIFIED = "unspecified", "Unspecified" 
        SOFT = "soft", "Soft" 
        SEMI_SOFT = "semi-soft", "Semi-Soft" 
        SEMI_HARD = "semi-hard", "Semi-Hard" 
        HARD = "hard", "Hard" 

    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

class Review(models.Model):
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(max_length=1000, blank=True)
    owner = models.ForeignKey('auth.User', null=True, related_name='reviews', on_delete=models.CASCADE)

    class ReviewScore(models.TextChoices): 
        UNSPECIFIED = "unspecified", "Unspecified" 
        STINKY = "stinky", "Stinky"
        MEH = "meh", "Meh" 
        OKAY = "okay", "Okay" 
        GOOD = "good", "Good" 
        FANTASTIC = "fantastic", "Fantastic"

    score = models.CharField("Review Score", max_length=20, choices=ReviewScore.choices, default=ReviewScore.UNSPECIFIED)

class Rating(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey('auth.User', null=True, related_name='ratings', on_delete=models.CASCADE)

    class Vote(models.IntegerChoices):
        UPVOTE = 1, 'Upvote'
        DOWNVOTE = -1, 'Downvote'

    vote = models.IntegerField(choices=Vote.choices)
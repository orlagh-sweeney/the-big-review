from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """ Review model """
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie_id = models.IntegerField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    review_likes = models.IntegerField(default=0)
    RATING = [
        (0, 'not rated'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    rating = models.IntegerField(choices=RATING, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class ReviewLikes(models.Model):
    """ Review likes model """
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_likes')
    LIKES = [
        (1, 'like'),
        (-1, 'dislike'),
    ]
    likes = models.IntegerField(choices=LIKES, default=0)

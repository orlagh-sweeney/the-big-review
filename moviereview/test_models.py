from django.test import TestCase
from .models import Review, ReviewLikes, User


class TestModels(TestCase):

    def test_review_model(self):
        user = User.objects.create_user(username='testuser', password='password')
        review = Review.objects.create(title='Test Review', author=user, movie_id='123', body='This is a review', rating='1')
        self.assertEqual(review.title, 'Test Review')
        self.assertEqual(review.author, user)
        self.assertEqual(review.movie_id, '123')
        self.assertEqual(review.body, 'This is a review')
        self.assertEqual(review.rating, '1')

    def test_reviewlikes_model(self):
        user = User.objects.create_user(username='testuser', password='password')
        review = Review.objects.create(title='Test Review', author=user, movie_id='123', body='This is a review', rating='1')
        reviewlike = ReviewLikes.objects.create(review=review, voter=user, likes='1')
        self.assertEqual(reviewlike.review, review)
        self.assertEqual(reviewlike.voter, user)
        self.assertEqual(reviewlike.likes, '1')

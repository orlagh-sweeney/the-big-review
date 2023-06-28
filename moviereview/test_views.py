from django.test import TestCase
from .models import Review, ReviewLikes, User


class TestHomeView(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestSearchResultsView(TestCase):

    def test_get_search_results_page(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')


class TestMovieDetailView(TestCase):

    def test_get_search_results_page(self):
        movie_id = 123
        response = self.client.get(f'/search/movie/{movie_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_detail.html')


class TestAddReviewView(TestCase):

    def test_get_add_review_page(self):
        movie_id = 123
        response = self.client.get(f'/search/movie/{movie_id}/addreview/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')

    def test_can_add_review(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/search/movie/{movie_id}/addreview/', {
            'title': 'Test Review',
            'author': user,
            'body': 'This is a review',
            'rating': '1'
        })
        self.assertRedirects(response, (f'/search/movie/{movie_id}/'))


class TestEditReviewView(TestCase):

    def test_get_add_review_page(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(username='testuser', password='password')
        review = Review.objects.create(
            title='Test Review',
            author=user,
            movie_id='123',
            body='This is a review',
            rating='1'
        )
        response = self.client.get(
            f'/search/movie/{movie_id}/edit/{review.id}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_review.html')

    def test_can_edit_review(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(username='testuser', password='password')
        review = Review.objects.create(
            title='Test Review',
            author=user,
            movie_id='123',
            body='This is a review',
            rating='1'
        )
        response = self.client.post(
            f'/search/movie/{movie_id}/edit/{review.id}',
            {
                'title': 'Test Review Updated',
                'author': user,
                'body': 'This is an updated review',
                'rating': '2'
            }
        )
        self.assertRedirects(response, (f'/search/movie/{movie_id}/'))
        updated_review = Review.objects.get(id=review.id)
        self.assertEqual(updated_review.title, 'Test Review Updated')


class TestDeleteReviewView(TestCase):

    def test_get_delete_review_page(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(username='testuser', password='password')
        review = Review.objects.create(
            title='Test Review',
            author=user,
            movie_id='123',
            body='This is a review',
            rating='1'
        )
        response = self.client.get(
            f'/search/movie/{movie_id}/delete/{review.id}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_review.html')

    def test_can_delete_review(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(username='testuser', password='password')
        review = Review.objects.create(
            title='Test Review',
            author=user,
            movie_id='123',
            body='This is a review',
            rating='1'
        )
        response = self.client.post(
            f'/search/movie/{movie_id}/delete/{review.id}'
        )
        self.assertRedirects(response, (f'/search/movie/{movie_id}/'))
        existing_reviews = Review.objects.filter(id=review.id)
        self.assertEqual(len(existing_reviews), 0)


class TestReviewLikeView(TestCase):

    def test_can_like_review(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(username='testuser', password='password')
        review = Review.objects.create(
            title='Test Review',
            author=user,
            movie_id='123',
            body='This is a review',
            rating='1'
        )
        reviewlike = ReviewLikes.objects.create(
            review=review, voter=user, likes='1'
        )
        response = self.client.post(f'/like/{review.id}')
        self.assertRedirects(response, (f'/search/movie/{movie_id}/'))

    def test_can_unlike_review(self):
        movie_id = 123
        user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client.login(
            username='testuser',
            password='password'
        )
        review = Review.objects.create(
            title='Test Review',
            author=user,
            movie_id='123',
            body='This is a review',
            rating='1'
        )
        reviewlike = ReviewLikes.objects.create(
            review=review,
            voter=user,
            likes='1'
        )
        response = self.client.post(f'/like/{review.id}')
        self.assertRedirects(response, (f'/search/movie/{movie_id}/'))
        existing_likes = ReviewLikes.objects.filter(id=reviewlike.id)
        self.assertEqual(len(existing_likes), 0)

from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_review_title_is_required(self):
        form = ReviewForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_review_body_is_required(self):
        form = ReviewForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_review_rating_is_required(self):
        form = ReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ['title', 'body', 'rating'])

from .modesl import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """ From to submit a movie review """
    rating_choices = [
        (0, 'not rated'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
        ]
    rating = forms.IntegerField(
        widget=forms.RadioSelect(choices=rating_choices),
        required=True
    )

    class Meta:
        model = Review
        fields = [
            'title',
            'body',
            'rating',
            ]

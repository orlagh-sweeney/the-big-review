from django.contrib import admin
from .models import Review, ReviewLikes
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_filter = ('created_on', 'rating')
    list_display = ('author', 'title', 'created_on', 'updated_on', 'rating', 'movie_id')
    search_fields = ('title', 'body', 'email', 'author')
    summernote_fields = ('body')


@admin.register(ReviewLikes)
class ReviewLikesAdmin(admin.ModelAdmin):
    list_display = ('voter', 'review', 'likes')
    search_fields = ('voter', 'review')
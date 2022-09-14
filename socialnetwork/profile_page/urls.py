from django.urls import path
from .views import profile_page, create_profile, update_profile, create_post, update_post, delete_post

urlpatterns = [
    path('', profile_page, name='profile'),
    path('create', create_profile, name='create_profile'),
    path('update', update_profile, name='update_profile'),
    path('post/create', create_post, name='create_post'),
    path('post/update/<post_id>', update_post, name='update_post'),
    path('post/delete/<post_id>', delete_post, name='delete_post')
]
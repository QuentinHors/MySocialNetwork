from django.urls import path
from .views import profile_page, create_or_update_profile

urlpatterns = [
    path('', profile_page, name='profile'),
    path('create', create_or_update_profile, name='create_or_update_profile'),
]
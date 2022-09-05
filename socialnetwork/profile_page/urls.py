from django.urls import path
from .views import profile_page, create_profile, update_profile

urlpatterns = [
    path('', profile_page, name='profile'),
    path('create', create_profile, name='create_profile'),
    path('update', update_profile, name='update_profile')
]
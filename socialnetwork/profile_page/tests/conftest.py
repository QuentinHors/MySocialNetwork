import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data():
    return {'email': 'email@email.com', 'username': 'username', 'password': 'pass'}


@pytest.fixture
def create_test_user(user_data):
    test_user = get_user_model().objects.create_user(**user_data)
    return test_user


@pytest.fixture
def login_user(client, create_test_user, user_data):
    user = create_test_user
    client.login(email=user_data['email'], password=user_data['password'])
    return user

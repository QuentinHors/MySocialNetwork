import pytest
from django import urls
from django.contrib.auth import get_user_model
from profile_page.models import Profile

User = get_user_model()


@pytest.mark.django_db(transaction=True)
def test_create_and_update_profile(client):
    user = User.objects.create_user(email='email@email.com', username='username', password='pass')
    client.login(email='email@email.com', password='pass')
    url = urls.reverse('profile')
    resp = client.get(url)
    assert resp.status_code == 200
    assert """<a href="/profile/create">""".encode('utf-8') in resp.content

    url = urls.reverse('create_profile')

    resp = client.post(url, {'first_name': 'first_name',
                             'last_name': 'last_name',
                             'description': 'description'})

    assert resp.status_code == 302

    try:
        profile = Profile.objects.get(user__id=user.id)
        assert profile.first_name == 'first_name'
        assert profile.last_name == 'last_name'
        assert profile.description == 'description'
    except Profile.DoesNotExist as exc:
        assert False, f"Get profile raised {exc}"

    # Zone update après création du profile

    url = urls.reverse('profile')
    resp = client.get(url)
    assert resp.status_code == 200
    assert """<a href="/profile/update">""".encode('utf-8') in resp.content

    url = urls.reverse('create_profile')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('update_profile')

    resp = client.post(resp.url, {'first_name': 'first_name_modified',
                                  'last_name': 'last_name_modified',
                                  'description': 'description_modified'})

    assert resp.status_code == 302

    try:
        profile = Profile.objects.get(user__id=user.id)
        assert profile.first_name == 'first_name_modified'
        assert profile.last_name == 'last_name_modified'
        assert profile.description == 'description_modified'
    except Profile.DoesNotExist as exc:
        assert False, f"Get profile raised {exc}"

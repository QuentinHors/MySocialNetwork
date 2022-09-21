import pytest
from profile_page.models import Post
from django import urls


@pytest.mark.django_db
def test_create_post(client, login_user):
    user = login_user
    url = urls.reverse('create_post')
    resp = client.get(url)
    assert resp.status_code == 200
    resp = client.post(url, {'text': 'ceci est un post!', 'next': urls.reverse('home')})
    assert resp.status_code == 302
    try:
        post = Post.objects.get(user__id=user.id)
        assert post.text == 'ceci est un post!'
    except Post.DoestNotExist as exc:
        assert False, f'Get Post raised {exc}'

    return user, post


@pytest.mark.django_db
def test_update_post(client, login_user):
    user, post = test_create_post(client, login_user)
    url = urls.reverse('update_post', kwargs={'post_id': post.id})
    resp = client.get(url)
    assert resp.status_code == 200
    resp = client.post(url, {'text': 'ceci est un nouveau post!', 'next': urls.reverse('home')})
    assert resp.status_code == 302
    try:
        post = Post.objects.get(user__id=user.id, id=post.id)
        assert post.text == 'ceci est un nouveau post!'
    except Post.DoestNotExist as exc:
        assert False, f'Get Post raised {exc}'


@pytest.mark.django_db
def test_delete_post(client, login_user):
    user, post = test_create_post(client, login_user)
    url = urls.reverse('delete_post', kwargs={'post_id': post.id})
    resp = client.get(url, {'next': urls.reverse('home')})
    assert resp.status_code == 302
    with pytest.raises(Post.DoesNotExist):
        Post.objects.get(user__id=user.id, id=post.id)
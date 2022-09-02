import pytest
from account.models import CustomUser
from django.db.utils import IntegrityError


@pytest.mark.django_db(transaction=True)
def test_create_superuser():
    superuser = CustomUser.objects.create_superuser(email='test@test.com', username='test',
                                                    password='test')
    assert superuser.email == 'test@test.com'
    assert superuser.username == 'test'
    assert superuser.is_superuser
    assert superuser.is_staff
    assert superuser.is_active

    with pytest.raises(IntegrityError):
        # Doit raise une IntegrityError sur le champ email
        CustomUser.objects.create_superuser(email='test@test.com', username='test2',
                                            password='test')
    with pytest.raises(IntegrityError):
        # Doit raise une IntegrityError sur le champ username
        CustomUser.objects.create_superuser(email='test2@test.com', username='test',
                                            password='test')
    with pytest.raises(ValueError):
        CustomUser.objects.create_superuser(email='', username='test2', password='test')

    with pytest.raises(ValueError):
        CustomUser.objects.create_superuser(username='', email='test2@test.com', password='test')


@pytest.mark.django_db(transaction=True)
def test_create_user():
    user = CustomUser.objects.create_user(email='test@test.com', username='test', password='test')

    assert user.email == 'test@test.com'
    assert user.username == 'test'
    assert not user.is_superuser
    assert not user.is_staff
    assert user.is_active

    with pytest.raises(IntegrityError):
        # Doit raise une IntegrityError sur le champ email
        CustomUser.objects.create_user(email='test@test.com', username='test2', password='test')

    with pytest.raises(IntegrityError):
        # Doit raise une IntegrityError sur le champ username
        CustomUser.objects.create_user(email='test2@test.com', username='test', password='test')

    with pytest.raises(ValueError):
        CustomUser.objects.create_user(email='', username='test2', password='test')

    with pytest.raises(ValueError):
        CustomUser.objects.create_user(username='', email='test2@test.com', password='test')

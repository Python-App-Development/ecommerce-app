import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    create django admin user
    """
    return django_user_model.objects.create_superuser(
        "root", "muzammilpeer987@gmail.com", "pa5is8an"
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    setup db
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")

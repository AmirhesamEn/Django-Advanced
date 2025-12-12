from datetime import datetime
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
import pytest


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="test@testtest.com", password="1234", is_active=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "the king in the north",
            "content": "content",
            "status": True,
            "published_date": "2025-01-01T10:00:00Z",
        }
        response = api_client.post(url, data=data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "the king in the north",
            "content": "content",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data=data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400(self, api_client,
                                                   common_user):
        url = reverse("blog:api-v1:post-list")
        data = {"title": True, "content": "wow"}
        user = common_user
        api_client.force_login(user)
        response = api_client.post(url, data=data)
        assert response.status_code == 401

from django.test import TestCase
from blog.models import Post
from accounts.models import Profile, User
from datetime import datetime


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com", password="test_test"
        )
        self.profile = Profile.objects.create(
            user=self.user, first_name="test", last_name="test", description="test"
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="test",
            content="content",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, "test")
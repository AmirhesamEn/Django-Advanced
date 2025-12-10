from datetime import datetime
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Category
from accounts.models import User, Profile

class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user( email="test@test.com", password="test_test", is_active = True)
        self.profile = Profile.objects.create(
            user=self.user, first_name="test", last_name="test", description="test"
        )
        
        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="content",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
    def test_blog_index_url_successful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # print(str(response.content))
        self.assertTrue("Hello" in response.content.decode())
        self.assertTemplateUsed(response, template_name="blog/test.html")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk":self.post.id})
        response = self.client.get(url)
        print(url)
        print(response)
        self.assertEqual(response.status_code, 200)
    
    def test_blog_post_detail_anonymous_in_response(self):
        url = reverse("blog:post-detail", kwargs={"pk":self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
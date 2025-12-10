from django.test import SimpleTestCase, TestCase
from datetime import datetime

from ..forms import PostForm
from ..models import Category

class TestPostForm(TestCase):
    
    def test_post_form_with_valid_deta(self):
        category_obj = Category.objects.create(name="hello2")
        form = PostForm(data={
            "title":"i am joffry",
            "content":"house of stark",
            "status":True,
            "category":category_obj,
            "published_date":datetime.now()
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_deta(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
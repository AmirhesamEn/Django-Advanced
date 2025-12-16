import random
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category
from django.db import transaction
category_list = [
    "IT",
    "Design",
    "Fun"
]

class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()
    
    @transaction.atomic 
    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),
        password="Test2025", is_active=True, is_verified=True)
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save() 

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author = profile,
                title = self.fake.sentence(nb_words=6),
                content = self.fake.paragraph(nb_sentences=10),
                status = self.fake.boolean(),
                category = Category.objects.get(name=random.choice(category_list)),
                published_date = timezone.now()

            )
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog_app.models import Post, Comment
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate dummy data for the blog app'

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_users = 5
        num_posts = 10
        num_comments = 20

        # Create dummy users
        users = []
        for _ in range(num_users):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user {user.username}'))

        # Create dummy posts
        posts = []
        for _ in range(num_posts):
            post = Post.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                author=random.choice(users)
            )
            posts.append(post)
            self.stdout.write(self.style.SUCCESS(f'Created post "{post.title}"'))

        # Create dummy comments
        for _ in range(num_comments):
            Comment.objects.create(
                content=fake.text(),
                post=random.choice(posts),
                author=random.choice(users)
            )
            self.stdout.write(self.style.SUCCESS('Created a comment'))

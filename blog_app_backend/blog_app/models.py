from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a blog post.
    Fields:
    - title: The title of the post.
    - content: The content of the post.
    - author: The user who authored the post.
    - created_at: Timestamp when the post was created.
    - updated_at: Timestamp when the post was last updated.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the post.
        The string representation is the title of the post.
        """
        return self.title


class Comment(models.Model):
    """
    Represents a comment on a blog post.
    Fields:
    - post: The post this comment is related to.
    - content: The content of the comment.
    - author: The user who authored the comment.
    - created_at: Timestamp when the comment was created.
    - updated_at: Timestamp when the comment was last updated.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the comment.

        The string representation includes the author and the post on which the comment was made.
        """
        return f"Comment by {self.author} on {self.post}"

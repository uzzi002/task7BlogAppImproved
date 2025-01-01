from django.db import models

class Post(models.Model):
    """
    Represents a blog post in the application.
    Attributes:
        title (str): The title of the blog post.
        content (str): The main content of the blog post.
        date_posted (datetime): The timestamp when the post was created.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=140, default='Your default quote or name')

    def __str__(self):
        return self.title

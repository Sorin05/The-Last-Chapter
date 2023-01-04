from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """
    Class defining the fields in BlogPost model
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.title)


class Comment(models.Model):
    """
    Class defining the fields in Comment
    """

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_article = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_body = models.TextField(max_length=200)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.comment_body)

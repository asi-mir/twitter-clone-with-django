from django.db import models
from accounts.models import Profile
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, related_name='author')

    body = models.TextField()

    liked = models.ManyToManyField(Profile, default=None, blank=True, related_name='liked')

    creat_date = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=type)

    tags = TaggableManager()

    def __str__(self):
        return str(self.body)

    @property
    def get_liked(self):
        return self.liked.all()

    @property
    def like_count(self):
        return self.liked.all().count()


class Files(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    files = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.post.body + 'File'

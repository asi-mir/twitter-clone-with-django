import os

from django.db import models
from accounts.models import Profile , User
from taggit.managers import TaggableManager


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='author')

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


def file_path_dir(instance, filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)

    return "uploaded/user/post" + "/" + str(instance.post.author) + "/" + str(ext) + "/" + filename


class Files(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    files = models.FileField(upload_to=file_path_dir, null=True, blank=True)

    def __str__(self):
        return self.post.body + 'File'

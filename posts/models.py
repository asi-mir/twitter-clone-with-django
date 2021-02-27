from django.db import models
from accounts.models import Profile


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=False, related_name='author')
    picture = models.ImageField(upload_to='images', blank=True)
    body = models.TextField()
    liked = models.ManyToManyField(Profile, default=None, blank=True, related_name='liked')
    creat_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)

    def get_liked(self):
        return self.liked.all()

    @property
    def like_count(self):
        return self.liked.all().count()

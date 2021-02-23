from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    content = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True)
    #restriction = models.Choices(["FOLLOWERS":FOLLOWERS,"FOLLOWING":FOLLOWING,"MENTIONED":MENTIONED])
    # def __str__(self):
    #     return self.content
    class Meta:
        ordering = ['-id']
    def serialize(self):
        return{
        "id":self.id,
        "content":self.content,
        "likes":random.randint(0,200)
        }
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True)
    #restriction = models.Choices(["FOLLOWERS":FOLLOWERS,"FOLLOWING":FOLLOWING,"MENTIONED":MENTIONED])
    
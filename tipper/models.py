from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    address = models.CharField(max_length=155)
    first_name = models.CharField(max_length=55)
    last_initial = models.CharField(max_length=5)
    bill = models.FloatField()
    tip = models.FloatField()
    post= models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return 'Post {} by {}'.format(self.post, self.first_name)

class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    comment = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment')
    post_comment = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment')

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

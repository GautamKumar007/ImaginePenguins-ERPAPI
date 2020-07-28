from django.db import models
from UserApi.models import User
from django.utils import timezone
# Create your models here.

class Feed(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=2**16, default='')
    post_time = models.DateTimeField(default=timezone.now)
    img = models.CharField(max_length=200, null=True, default='')
    

class Tag(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)

class Feed_Tag(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    feed_tags = models.ForeignKey(Feed, on_delete=models.CASCADE)
    tag_tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Feed_Like(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE)

class Comment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2**10)

class Comments_Comment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, name='some comment')

class Comments_Like(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


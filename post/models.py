from django.db import models
from django.contrib.auth.models import User
from account.models import Account
# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    # image = models.ImageField()
    
    like_by = models.ManyToManyField(Account,blank=True)
    post_likes_count = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,blank=True,null=True,related_name="comments",on_delete=models.SET_NULL)
    comment_text = models.TextField()
    user = models.ForeignKey(Account,blank=True,null=True,on_delete=models.CASCADE,related_name="comments")
    likes = models.ManyToManyField(Account,blank=True)
    coment_likes_count = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.comment_text

class ReplyComment(models.Model):
    reply_text =models.TextField(blank=True)
    comment = models.ForeignKey(Comment,related_name="replies",blank=True,null=True,on_delete=models.SET_NULL)
    likes_by = models.ManyToManyField(Account,blank=True)
    user = models.ForeignKey(Account,blank=True,null=True,on_delete=models.CASCADE,related_name="replies")
    reply_likes_count = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.reply_text





from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,default='')

    feat_img = models.ImageField(upload_to='media',blank=True)
    created_at = models.DateTimeField('date published',auto_now=True)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class PostComment(models.Model):
    comment_post = models.ForeignKey(BlogPost,on_delete=models.DO_NOTHING)
    comment_body = models.TextField()
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    posted_at = models.DateTimeField('time posted',auto_now=True)
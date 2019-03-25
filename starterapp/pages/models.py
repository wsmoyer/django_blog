from django.db import models

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250,null=True)
    body = models.TextField()
    feat_img = models.ImageField(upload_to='media', null=True,blank=True)
    def __str__(self):
        return self.title
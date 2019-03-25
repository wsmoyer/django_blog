from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category,BlogPost,PostComment
# Register your models here.




admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(PostComment)

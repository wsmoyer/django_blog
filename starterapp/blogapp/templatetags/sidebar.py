from django import template
from blogapp.models import Category,BlogPost

register = template.Library()


@register.simple_tag
def category_sidebar():
    category_list = Category.objects.all()
    return category_list
@register.simple_tag
def archive_sidebar(request,post_date):
    post_date_list = BlogPost.objects.all().filter(post_date=created_at)
from django import template
from pages.models import Pages

register = template.Library()


@register.simple_tag
def navbar():
    page_list = Pages.objects.all()
    return page_list
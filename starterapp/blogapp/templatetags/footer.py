from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag()
def footer():
    currentYear = datetime.now().year
    return currentYear
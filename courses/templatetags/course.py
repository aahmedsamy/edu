from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None


@register.filter
def is_instructor(user):
    return user.groups.filter(name='Instructors').exists()


@register.filter
def ckeditor(html):
    return mark_safe(html)

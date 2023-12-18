from django import template

register = template.Library()

@register.simple_tag
def first_tag():
    list = {
        'test': 'Mersedes'
    }
    return list
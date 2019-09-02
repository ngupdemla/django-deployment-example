from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """This cuts the value n teh arg"""
    return value.replace(arg, '')

# register.filter('cut',cut)

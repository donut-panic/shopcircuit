from django import template

register = template.Library()

@register.filter(is_safe=True)
def add_float(value, arg):
    """Dodaje liczby ale float"""
    return f'{float(value) + float(arg):.2f}'

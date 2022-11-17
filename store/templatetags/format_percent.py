from django import template

register = template.Library()


@register.filter(is_safe=True)
def format_percent(value):
    return f"{int(float(value) * 100)}%"

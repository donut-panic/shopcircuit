from django import template

register = template.Library()


@register.filter
def format_percent(value):
    return f"{int(float(value) * 100)}%"

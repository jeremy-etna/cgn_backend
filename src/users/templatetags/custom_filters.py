from django import template

register = template.Library()


@register.filter
def remove_spaces(value):
    return value.replace(" ", "")

@register.filter
def underscore_to_space(value):
    return value.replace("_", " ")
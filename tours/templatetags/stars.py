from django import template

register = template.Library()


@register.filter()
def stars(num_stars):
    return int(num_stars) * chr(9733)

from django import template

register = template.Library()


@register.filter()
def min_val(list_of_num):
    return min(list_of_num)


@register.filter()
def max_val(list_of_num):
    return max(list_of_num)

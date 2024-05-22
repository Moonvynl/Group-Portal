from django import template

register = template.Library()


@register.filter
def get_days_row(row, days_of_month):
    if row == 1:
        days = range(1, 8)
    elif row in [2, 3, 4]:
        days = range(7*(row-1)+1, 7*row + 1)
    elif days_of_month != 28:
        days = range(29, days_of_month)
    return days

@register.filter
def get_range(value):
    return range(1, value+1)

import datetime

from django import template

register = template.Library()


@register.filter
def post_time(create_time):
    last_date = datetime.datetime.now() - datetime.timedelta(1)
    if create_time:
        if create_time.strftime('%Y-%m-%d-%H:%M:%S')\
                >= last_date.strftime('%Y-%m-%d-%H:%M:%S'):
            return True
    else:
        return False


@register.filter
def plus_days(value, days):
    return value + datetime.timedelta(days=days)

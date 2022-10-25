"""BKSP > utils.py"""
# PYTHON IMPORTS
import logging
from typing import Union
# from django.core.cache import cache
# from django.contrib.auth.models import Group

logger = logging.getLogger(__name__)


# def user_has_group(user, group_name):
#     if cache.get('user_groups') is None:
#         cache.set('user_groups', list(
#             Group.objects.values('user__id', 'user__groups__name')
#         ), 200)
#     user_groups = cache.get('user_groups')
#     return {'user__id': user.id, 'user__groups__name': group_name
#             } in user_groups


def user_has_group(user, group_name):
    if user.groups.filter(name=group_name).exists():
        return True
    else:
        return False


def get_percentage(part: Union[int, float], whole: Union[int, float]) -> int:
    """
    return obtained mark percent in int
    formula = 100 * part . whole
    i.e = 100 * 40 / 50 = 80
    """
    percent = 100 * float(part) / float(whole)
    return int(percent)

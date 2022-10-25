from django import template
from utilities.utils import user_has_group
from utilities.variables import (
    group_teacher,
    group_employee,
    group_coach,
    group_admin,
    group_guardian,
    group_bksp,
    group_bkp

)
register = template.Library()


@register.filter
def is_bksp(user):
    return user_has_group(user, group_bksp)


@register.filter
def is_bkp(user):
    return user_has_group(user, group_bkp)


@register.filter
def is_admin(user):
    return user_has_group(user, group_admin)


@register.filter
def is_employee(user):
    return user_has_group(user, group_employee)


@register.filter
def is_coach(user):
    return user_has_group(user, group_coach)


@register.filter
def is_teacher(user):
    return user_has_group(user, group_teacher)


@register.filter
def is_guardian(user):
    return user_has_group(user, group_guardian)

from django import template
register = template.Library()


@register.filter
def get_register_subject(ac_trainee, ac_class):
    """Finding total Subject and pass mark  of send game"""
    if ac_trainee and ac_class:
        return ac_trainee.trainee.registration_trainee.filter(
            academic_class=ac_class
        ).values_list("subject__name", flat=True)

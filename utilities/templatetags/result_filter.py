from django import template
register = template.Library()


@register.filter
def class_filter(obj_list, all_class):
    """For all value of the  list all_class
     all_class[0] = classes
     all_class[1] = session
     all_class[2] = exam
     This index Point is Fixed only for passing multiple
    pram in this system
     """
    classes = all_class[0]
    session = all_class[1]
    exam = all_class[2]
    if obj_list:
        obj_list = obj_list
        if classes:
            obj_list = obj_list.filter(classes__classes__pk=classes)
        if session:
            obj_list = obj_list.filter(classes__session__pk=session)
        if exam:
            obj_list = obj_list.filter(examination__pk=exam)
        return obj_list


@register.filter
def class_total_marks(obj_list, all_class):
    """For all value of the  list all_class
     all_class[0] = classes
     all_class[1] = session
     all_class[2] = exam
     This index Point is Fixed only for passing multiple
    pram in this system
     """
    total = 0
    classes = all_class[0]
    session = all_class[1]
    exam = all_class[2]
    if obj_list and classes and session and exam:
        obj_list = obj_list
        if classes:
            obj_list = obj_list.filter(classes__classes__pk=classes)
        if session:
            obj_list = obj_list.filter(classes__session__pk=session)
        if exam:
            obj_list = obj_list.filter(examination__pk=exam)
    for obj in obj_list:
        if obj.marks:
            total += obj.marks
    return total

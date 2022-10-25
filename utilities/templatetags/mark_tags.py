from django import template

register = template.Library()


@register.filter(name='get_total_mark')
def total_mark(object_list, all_subject):
    total = 0
    if object_list and all_subject:
        for subject in all_subject:
            my_object = object_list.select_related(
                "subject"
            ).filter(subject=subject)
            for marks in my_object:
                total += marks.marks
    return round(total)


@register.filter
def total_highest_mark(all_subject):
    total = 0
    if all_subject:
        for subject in all_subject:
            if subject.highest_mark:
                total += subject.highest_mark
    return round(total)


@register.filter
def get_subject_data(object, subject):
    if object and subject:
        return object.trainee.get_all_mark.filter(subject=subject).distinct()


@register.filter
def get_academic_class_marks(object, academic_class):
    if object and academic_class:
        return object.trainee.get_filter_marks(academic_class)


@register.filter
def get_academic_class_game_marks(object, academic_class):
    if object and academic_class:
        return object.trainee.get_filter_game_marks(academic_class)


@register.filter
def get_subject_marks(object_list, subject):
    total = 0
    if object_list and subject:
        object_list = object_list.filter(subject=subject)
        for marks in object_list:
            total += marks.marks
    return round(total)


@register.filter
def get_game_subject_mark(object_list, subject):
    mark = 0
    if object_list and subject:
        object_list = object_list.filter(subject=subject)
        for marks in object_list:
            mark = marks.marks
    return round(mark)


@register.filter
def get_game_subject_total_mark(object_list):
    total = 0
    if object_list:
        for marks in object_list:
            total += marks.marks
    return round(total)


@register.filter
def get_exam_marks(object_list, exam):
    total = 0
    if object_list and exam:
        object_list = object_list.filter(examination=exam)
        for marks in object_list:
            total += marks.marks
    return round(total)


@register.filter
def get_grade(mark, grade_list):
    if mark and grade_list:
        for grade in grade_list:
            if grade.start_level >= mark >= grade.end_level:
                return grade.grade
    return "Need more data"


@register.filter
def get_total_grade(mark, grade_list):
    if mark and grade_list:
        for grade in grade_list:
            if mark >= grade.points:
                return grade.grade
            pass
    return "Need more data"


@register.filter
def get_grade_point(mark, grade_list):
    if mark and grade_list:
        for grade in grade_list:
            if grade.start_level >= mark >= grade.end_level:
                return grade.points
    return "Need more data"


@register.filter
def get_subjects(object_list, all_subject):
    gp = []
    if object_list and all_subject:
        for subject in all_subject:
            my_object = object_list.filter(subject=subject)
            total = 0
            for marks in my_object:
                total += marks.marks
            gp.append(round(total))
    return gp


@register.filter
def get_gp(object_list, grade_list):
    if object_list and grade_list:
        total = 0
        for mark in object_list:
            for grade in grade_list:
                if grade.start_level >= mark >= grade.end_level:
                    total += grade.points
                    break
        return total
    return "Need more data"


@register.filter
def get_gpa(object_list, grade_list):
    total = 0
    if object_list and grade_list:
        for mark in object_list:
            for grade in grade_list:
                if grade.start_level >= mark >= grade.end_level:
                    total += grade.points
                    break
        return round(total / len(object_list), 2)
    return total


@register.filter
def get_marks_type(object_list, marks_type):
    if object_list and marks_type:
        return object_list.filter(marks_type=marks_type)


@register.filter
def get_trainee_marks(object_list, trainee):
    if object_list and trainee:
        return object_list.filter(trainee=trainee)


@register.filter
def get_trainee_marks_total(object_list, trainee):
    total = 0
    if object_list and trainee:
        object_list = object_list.filter(trainee=trainee)
        for mark in object_list:
            total += mark.marks
        return round(total)
    return "Need more data"

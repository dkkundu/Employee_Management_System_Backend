from django import template
from decimal import Decimal
from academic.models import ExaminationSubject

register = template.Library()


@register.filter
def get_academic_subject(obj_list, academic_class):
    """Finding total result of sending game"""
    if obj_list and academic_class:
        return obj_list.filter(academic_class=academic_class)


@register.filter
def get_existing_marks(total_subject_marks, total_marks):
    if total_subject_marks and total_marks:
        return int(total_marks) - int(total_subject_marks)


@register.filter
def get_total_subject_marks(subject, academic_class):
    total = Decimal(0)
    if subject and academic_class:
        subject_all = ExaminationSubject.objects.select_related("exam").filter(
            exam__academic_class=academic_class, subject=subject
        )
        for sub in subject_all:
            if sub.highest_mark:
                total += sub.highest_mark
    return total


@register.filter
def get_subject_marks(exam, subject):
    total = 0
    if exam and subject:
        all_marks = exam.examination.filter(subject=subject)
        for exam_mark in all_marks:
            total += exam_mark.highest_mark
    return total


@register.filter
def get_independent_subject_marks(exam, subject):
    total = 0
    if exam and subject:
        all_marks = exam.independent_examination.filter(subject=subject)
        for exam_mark in all_marks:
            total += exam_mark.highest_mark
    return total


@register.filter
def get_subject_teacher(academic_class, subject):
    if academic_class and subject:
        return academic_class.academicclassteacher_set.filter(subject=subject)

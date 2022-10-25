import logging
from django import template
from academic.models import GradeCalculator

register = template.Library()
logger = logging.getLogger(__name__)


@register.filter
def get_register_subject(ac_trainee, exam):
    ac_class = ac_trainee.academic_class
    trainee = ac_trainee.trainee
    subject_list = []
    for registration in trainee.registration_trainee.filter(
            academic_class=ac_class
    ):
        if exam.examination.filter(subject=registration.subject).exists():
            subject_list.append(registration.subject)
    return subject_list


@register.filter
def total_marks_in_percentages(ac_trainee, exam):
    ac_class = ac_trainee.academic_class
    trainee = ac_trainee.trainee
    grade_point = None
    if ac_trainee.academic_class.classes.grade_system == 1:
        grade_point = GradeCalculator.objects.active_gpa()
    if ac_trainee.academic_class.classes.grade_system == 2:
        grade_point = GradeCalculator.objects.active_cgpa()

    subject_list = []
    for registration in trainee.registration_trainee.select_related(
        'subject',
    ).filter(
            academic_class=ac_class
    ):
        if exam.examination.filter(subject=registration.subject).exists():
            subject_total = float(0.0)
            marks_obtained = float(0.0)
            for marks in exam.examination.filter(subject=registration.subject):
                subject_total = subject_total + float(marks.highest_mark)

            for marks in trainee.mark_set.filter(academic_class=ac_class,
                                                 examination=exam,
                                                 subject=registration.subject):  # noqa
                marks_obtained = marks_obtained + float(marks.marks)
            in_percentages = (marks_obtained / subject_total) * 100
            gpa = ""
            point = ""
            if grade_point:
                try:
                    grad = grade_point.filter(
                        start_level__gte=in_percentages,
                        end_level__lte=in_percentages
                    ).first()
                    if grad:
                        gpa = grad.grade
                        point = grad.points
                except Exception as e:
                    logger.info(
                        f"grad not Found for {in_percentages} issue {e}"
                    )

            data_dir = {
                "subject": registration.subject,
                "subject_total": int(subject_total),
                "marks_obtained": int(marks_obtained),
                "marks_details": trainee.mark_set.select_related(
                    'academic_class', 'trainee', 'subject', "examination",
                    "marks_type"
                ).filter(
                    academic_class=ac_class, examination=exam,
                    subject=registration.subject
                ),
                "in_percentages": int(in_percentages),
                "gpa": gpa,
                "point": point,
                "grade_point": grade_point,
            }
            subject_list.append(data_dir)
    return subject_list


@register.filter
def total_marks_in_percentages_independent_exam(ac_trainee, exam):
    ac_class = ac_trainee.academic_class
    trainee = ac_trainee.trainee
    grade_point = None
    if ac_trainee.academic_class.classes.grade_system == 1:
        grade_point = GradeCalculator.objects.active_gpa()
    if ac_trainee.academic_class.classes.grade_system == 2:
        grade_point = GradeCalculator.objects.active_cgpa()

    subject_list = []
    for registration in trainee.registration_trainee.select_related(
        'academic_class', 'subject', 'trainee', "trainee_assign_id"
    ).filter(
            academic_class=ac_class
    ):
        if exam.independent_examination.select_related(
            'exam', 'subject', 'marks_type'
        ).filter(subject=registration.subject).exists():  # noqa
            subject_total = float(0.0)
            marks_obtained = float(0.0)
            for marks in exam.independent_examination.select_related(
                'exam', 'subject', 'marks_type'
            ).filter(subject=registration.subject):  # noqa
                subject_total = subject_total + float(marks.highest_mark)

            for marks in trainee.independentmark_set.select_related(
                    'academic_class', 'trainee', 'subject', "examination",
                    "marks_type"
            ).filter(
                    academic_class=ac_class, examination=exam,
                    subject=registration.subject):  # noqa
                marks_obtained = marks_obtained + float(marks.marks)
            in_percentages = (marks_obtained / subject_total) * 100
            gpa = ""
            point = ""
            if grade_point:
                try:
                    # range not math problem
                    grad = grade_point.filter(
                        start_level__gte=int(in_percentages),
                        end_level__lte=int(in_percentages)
                    ).first()
                    if grad:
                        gpa = grad.grade
                        point = grad.points
                except Exception as e:
                    logger.info(
                        f"grad not Found for {in_percentages} issue {e}"
                    )

            data_dir = {
                "subject": registration.subject,
                "subject_total": int(subject_total),
                "marks_obtained": int(marks_obtained),
                "marks_details": trainee.independentmark_set.filter(
                    academic_class=ac_class, examination=exam,
                    subject=registration.subject
                ),
                "in_percentages": int(in_percentages),
                "gpa": gpa,
                "point": point,
                "grade_point": grade_point,
            }
            subject_list.append(data_dir)
    return subject_list


@register.filter
def get_total_GPA(ac_trainee, exam):
    subject_list = total_marks_in_percentages(ac_trainee, exam)
    total_obtained = 0
    total_obtained_display = 0
    total_subject = 0
    total_grade = ""
    total_gpa = 0.00
    grade_list = []

    for obj in subject_list:
        grade_list.append(obj['gpa'])
        total_obtained += int(f"{obj['in_percentages']}")
        total_obtained_display += int(f"{obj['marks_obtained']}")
        total_subject += 1
        avg_point = (total_obtained / total_subject)

        if obj["grade_point"]:
            grad = obj["grade_point"].filter(
                start_level__gte=round(avg_point),
                end_level__lte=round(avg_point)
            ).first()
            total_grade = grad.grade if grad else ""
            total_gpa = grad.points if grad else ""

    total_list = [
        {
            # total calculations
            "total_marks": sum(
                [int(f"{obj['subject_total']}") for obj in subject_list]),
            # noqa
            "total_obtained": total_obtained_display,
            "total_grade": total_grade if "F" not in grade_list else "F",
            "total_gpa": total_gpa if "F" not in grade_list else "",
        }
    ]
    return total_list


@register.filter
def get_total_in_GPA(ac_trainee, exam):
    subject_list = total_marks_in_percentages_independent_exam(
        ac_trainee, exam
    )
    total_marks = sum([int(f"{obj['subject_total']}") for obj in subject_list])
    print(subject_list)
    total_obtained = 0
    total_obtained_real = 0
    total_subject = 0
    total_grade = ""
    total_gpa = 0.00
    grade_list = []
    for obj in subject_list:
        grade_list.append(obj['gpa'])
        total_obtained += int(f"{obj['in_percentages']}")
        total_obtained_real += int(f"{obj['marks_obtained']}")

        total_subject += 1
        avg_point = (total_obtained / total_subject)
        if obj["grade_point"]:
            grad = obj["grade_point"].filter(
                start_level__gte=round(avg_point),
                end_level__lte=round(avg_point)
            ).first()
            total_grade = grad.grade if grad else ""
            total_gpa = grad.points if grad else ""

    total_list = [
        {
            # total calculations
            "total_marks": total_marks,
            # noqa
            "total_obtained": total_obtained_real,
            "total_grade": total_grade if "F" not in grade_list else "F",
            "total_gpa": total_gpa if "F" not in grade_list else "",
        }
    ]
    return total_list


@register.filter
def total_independent_marks_in_percentages(ac_trainee, exam):
    ac_class = ac_trainee.academic_class
    trainee = ac_trainee.trainee
    grade_point = None
    if ac_trainee.academic_class.classes.grade_system == 1:
        grade_point = GradeCalculator.objects.active_gpa()
    if ac_trainee.academic_class.classes.grade_system == 2:
        grade_point = GradeCalculator.objects.active_cgpa()

    subject_list = []
    for registration in trainee.registration_trainee.filter(
            academic_class=ac_class
    ):
        if exam.independent_examination.filter(subject=registration.subject).exists():  # noqa 
            subject_total = float(0.0)
            marks_obtained = float(0.0)
            for marks in exam.independent_examination.filter(subject=registration.subject):  # noqa
                subject_total = subject_total + float(marks.highest_mark)

            for marks in trainee.independentmark_set.filter(
                academic_class=ac_class,
                examination=exam,
                subject=registration.subject
            ):
                marks_obtained = marks_obtained + float(marks.marks)
            in_percentages = (marks_obtained / subject_total) * 100
            gpa = ""
            point = ""
            if grade_point:
                try:
                    grad = grade_point.filter(
                        start_level__gte=in_percentages,
                        end_level__lte=in_percentages
                    ).first()
                    if grad:
                        gpa = grad.grade
                        point = grad.points
                except Exception as e:
                    logger.info(
                        f"grad not Found for {in_percentages} issue {e}"
                    )

            data_dir = {
                "subject": registration.subject,
                "subject_total": int(subject_total),
                "marks_obtained": int(marks_obtained),
                "marks_details": trainee.independentmark_set.filter(
                    academic_class=ac_class, examination=exam,
                    subject=registration.subject
                ),
                "in_percentages": int(in_percentages),
                "gpa": gpa,
                "point": point,
                "grade_point": grade_point,
            }
            subject_list.append(data_dir)
    return subject_list


@register.filter
def get_independent_total_gpa(ac_trainee, exam):
    subject_list = total_independent_marks_in_percentages(ac_trainee, exam)
    total_obtained = 0
    total_subject = 0
    total_grade = ""
    total_gpa = 0.00
    grade_list = []

    for obj in subject_list:
        grade_list.append(obj['gpa'])
        total_obtained += int(f"{obj['marks_obtained']}")
        total_subject += 1
        avg_point = (total_obtained / total_subject)

        if obj["grade_point"]:
            grad = obj["grade_point"].filter(
                start_level__gte=round(avg_point),
                end_level__lte=round(avg_point)
            ).first()
            total_grade = grad.grade if grad else ""
            total_gpa = grad.points if grad else ""

    total_list = [
        {
            # total calculations
            "total_marks": sum(
                [int(f"{obj['subject_total']}") for obj in subject_list]),
            # noqa
            "total_obtained": total_obtained,
            "total_grade": total_grade,
            "total_gpa": total_gpa,
            # "total_gpa": total_gpa if "F" not in grade_list else 0.00,
        }
    ]
    return total_list

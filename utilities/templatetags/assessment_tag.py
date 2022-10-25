from decimal import Decimal
from django import template
from assessment.models import (
    PreliminaryEvaluation,
    # FinalEvaluation,
    AcademicTestEvaluation
)
from subjects.models import MarkSystem

register = template.Library()


@register.filter
def game_wise_result(obj_list, game):
    """Finding total Subject and pass mark  of send game"""
    if obj_list:
        obj_list = obj_list
        if game:
            obj_list = obj_list.filter(game=game)
        return obj_list


@register.filter
def total_result_get(obj_list, game):
    """Finding total result of sending game"""
    total = Decimal(0)
    if obj_list:
        if game:
            obj_list = obj_list.filter(game=game)
        for pte_result in obj_list:
            if pte_result.marks:
                total += pte_result.marks
        return total


@register.filter
def total_subject_marks(obj_list, game):
    """Finding total subject marks of sending game"""
    total = Decimal(0)
    if obj_list:
        if game:
            obj_list = obj_list.filter(game=game)
        for pte_result in obj_list:
            if pte_result.subject:
                subject_mark = pte_result.subject.highest_mark
                total += subject_mark
        return total


@register.filter
def get_preliminary_total_result(applicant, game):
    """Finding preliminary total subject marks of a Applicant"""
    total = Decimal(0)
    if applicant and game:
        obj_list = PreliminaryEvaluation.objects.filter(
            applicant=applicant, game=game
        )
        for result in obj_list:
            if result.marks:
                total += result.marks
        return total


@register.filter
def get_preliminary_hight_mark(applicant, game):
    """Finding preliminary total subject marks of a Applicant"""
    total = Decimal(0)
    if applicant and game:
        obj_list = PreliminaryEvaluation.objects.filter(
            applicant=applicant, game=game
        )
        for result in obj_list:
            if result.subject.highest_mark:
                total += result.subject.highest_mark
        return total


@register.filter
def get_total_highest(obj_list):
    """Finding total subject marks"""
    total = Decimal(0)
    if obj_list:
        for pte_result in obj_list:
            if pte_result.highest_mark:
                total += pte_result.highest_mark
    return total


@register.filter
def get_total_marks(obj_list):
    """Finding total subject marks"""
    total = Decimal(0)
    if obj_list:
        for pte_result in obj_list:
            if pte_result:
                total += pte_result.marks
    return total


@register.filter
def get_subject(game, type):
    """Finding total Subject and pass mark  of send game"""
    if game and type:
        obj_list = game.get_children().filter(
            common_class=type, is_preliminary=True
        ).order_by("common_class__name")
        return obj_list


@register.filter
def get_skill_type_subject(game, skill):
    """Finding total Subject and pass mark  of send game"""
    if game and skill:
        obj_list = game.get_children().filter(
            single_skill_type=skill, is_long_term_trainees=True
        )
        return obj_list


@register.filter
def get_test_type_subject(ob_list, test):
    """Finding total Subject and pass mark  of send game"""
    if ob_list and test:
        return ob_list.filter(common_class=test)


@register.filter
def get_trainee_skills_type_subject(subject_list, skills):
    """Finding total Subject and pass mark  of send game"""
    if subject_list and skills:
        return subject_list.filter(single_skill_type=skills)


@register.filter
def get_subjects_result(game, application):
    """Finding total Subject and pass mark  of send game"""
    if game and application:
        obj_list = PreliminaryEvaluation.objects.filter(
            game=game, applicant=application
        )
        return obj_list


@register.filter
def get_type_result(obj_list, test_type):
    """Finding total Subject and pass mark  of send game"""
    if obj_list and test_type:
        ob_list = obj_list.filter(
            test_type=test_type
        )
        return ob_list


@register.filter
def get_final_subjects_result(game, application):
    """Finding total Subject and pass mark  of send game"""
    if game and application:
        obj_list = application.finalevaluation_set.select_related(
            "applicant", "subject", "game"
        ).filter(
            game=game
        )
        return obj_list


@register.filter
def get_final_total_result(applicant, game):
    """Finding preliminary total subject marks of a Applicant"""
    academic_total = Decimal(0)
    game_total = Decimal(0)
    if applicant and game:
        obj_game_marks_list = applicant.get_total_game_marks.filter(
            is_deleted=False, game=game
        )
        all_academic_result = applicant.get_total_academic_marks.filter(
            is_deleted=False, is_sports_science=False
        )
        for result in obj_game_marks_list:
            if result.marks:
                game_total += result.marks

        for result in all_academic_result:
            if result.marks:
                academic_total += result.marks

        return game_total + academic_total


@register.filter
def get_final_highest_mark(applicant, game):
    """Finding preliminary total subject highest marks of a Applicant"""
    academic_total = Decimal(0)
    game_total = Decimal(0)
    if applicant and game:
        obj_game_marks_list = applicant.get_total_game_marks.filter(
            is_deleted=False, game=game
        )
        all_academic_result = applicant.get_total_academic_marks.filter(
            is_deleted=False, is_sports_science=False
        )
        for result in obj_game_marks_list:
            if result.subject:
                game_total += result.subject.highest_mark

        for result in all_academic_result:
            if result.subject:
                academic_total += result.subject.highest_mark

        return game_total + academic_total


@register.filter
def get_final_academic_subject(applicant):
    """Finding preliminary total subject marks of a Applicant"""
    if applicant:
        obj_list = AcademicTestEvaluation.objects.filter(
            applicant=applicant, is_sports_science=False
        )
        return obj_list


@register.filter
def get_final_sports_science_subject(applicant):
    """Finding preliminary total subject marks of a Applicant"""
    if applicant:
        obj_list = AcademicTestEvaluation.objects.filter(
            applicant=applicant, is_sports_science=True
        )
        return obj_list


@register.filter
def get_percentages(obj_list, percent):
    """Finding preliminary total subject marks of a Applicant"""
    total = Decimal(0)
    if obj_list and percent:
        for obj in obj_list:
            if obj.marks:
                total += obj.marks
        total = (total * int(percent)) / 100
    return total


@register.filter
def get_game_academic_percentages(applicant, game):
    """Finding preliminary total subject marks of a Applicant"""
    academic_total = Decimal(0)
    game_total = Decimal(0)
    mark_system = MarkSystem.objects.get(
        is_active=True, is_deleted=False
    )
    if applicant and game:
        obj_game_marks_list = applicant.get_total_game_marks.filter(
            is_deleted=False, game=game
        )
        all_academic_result = applicant.get_total_academic_marks.filter(
            is_deleted=False, is_sports_science=False
        )
        for result in obj_game_marks_list:
            if result.marks:
                game_total += result.marks

        for result in all_academic_result:
            if result.marks:
                academic_total += result.marks
        game_total = (game_total * mark_system.game_percentages) / 100
        academic_total = (
                                 academic_total * mark_system.academic_percentages) / 100  # noqa

    return game_total + academic_total


@register.filter
def preliminary_type(type):
    """Finding preliminary total subject marks of a Applicant"""
    status = False
    if type:
        try:
            preliminary = type.common_class_subjects.filter(
                is_preliminary=True
            )
            if preliminary:
                status = True
        except Exception as e:
            print(f"Unable to get data {e}")
        return status


@register.filter
def final_type(type):
    """Finding preliminary total subject marks of a Applicant"""
    status = False
    if type:
        try:
            preliminary = type.common_class_subjects.filter(
                is_final=True
            )
            if preliminary:
                status = True
        except Exception as e:
            print(f"Unable to get data {e}")
        return status


@register.filter
def next_exist(loop_list, current_index):
    try:
        if loop_list[int(current_index) + 1]:
            return True
    except Exception as e:
        print(f"Unable to get data {e}")
        return False

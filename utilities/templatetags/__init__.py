from .post_time_tag import post_time
from .message_type_checker import message_check
from .group_checker_tag import (
    group_teacher,
    group_admin,
    group_coach,
    group_employee,
    is_bkp,
    is_bksp,
)
from .assessment_tag import (
    game_wise_result,
    total_result_get,
    total_subject_marks,
    get_preliminary_total_result,
    get_preliminary_hight_mark,
    get_total_marks,
    get_subject,
    get_subjects_result,
    get_final_subjects_result,
    get_final_total_result,
    get_final_highest_mark,
    get_final_academic_subject,
    get_final_sports_science_subject,
    preliminary_type,
    get_skill_type_subject,
    get_test_type_subject,
    get_trainee_skills_type_subject,
    next_exist,


)
from .result_filter import class_filter, class_total_marks
from .display_tags import (
    get_academic_subject,
    get_existing_marks,
    get_total_subject_marks,
    get_subject_teacher
)

from .mark_tags import (
    total_mark,
    get_subject_data
)
from .trainee_result import (
    get_register_subject,
    total_independent_marks_in_percentages,
    get_independent_total_gpa
)
from .get_register_subject import get_register_subject  # noqa

__all__ = [
    is_bkp,
    is_bksp,
    message_check,
    post_time,
    group_teacher,
    group_admin,
    group_coach,
    group_employee,
    class_filter,
    class_total_marks,
    game_wise_result,
    total_result_get,
    total_subject_marks,
    get_final_subjects_result,
    get_preliminary_total_result,
    get_preliminary_hight_mark,
    get_total_marks,
    get_subject,
    get_subjects_result,
    get_final_total_result,
    get_final_highest_mark,
    get_final_academic_subject,
    get_final_sports_science_subject,
    preliminary_type,
    get_skill_type_subject,
    get_test_type_subject,
    get_trainee_skills_type_subject,
    next_exist,

    get_academic_subject,
    get_existing_marks,
    get_total_subject_marks,
    get_subject_teacher,

    total_mark,
    get_subject_data,

    get_register_subject,
    total_independent_marks_in_percentages,
    get_independent_total_gpa
]

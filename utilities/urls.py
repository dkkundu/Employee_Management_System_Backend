"""utilities > urls.py"""
# DJANGO URLS
from utilities.views.index import AcademicIndex
from django.urls import path
# CORE IMPORTS
from .views import (
    CourtesyTitleListCreateView,
    CourtesyTitleDeleteView,
    CourtesyTitleUpdateView,

    DepartmentListCreateView,
    DepartmentDeleteView,
    DepartmentUpdateView,

    BranchListCreateView,
    BranchUpdateView,
    BranchDeleteView,

    TeacherDesignationsListCreateView,
    TeacherDesignationsDeleteView,
    TeacherDesignationsUpdateView,

    CoachDesignationsListCreateView,
    CoachDesignationsUpdateView,
    CoachDesignationsDeleteView,

    EmployeeDesignationsListCreateView,
    EmployeeDesignationsDeleteView,
    EmployeeDesignationsUpdateView,

    JobTypeListCreateView,
    JobTypeUpdateView,
    JobTypeDeleteView,

    CurrentWorkStatusCreateView,
    CurrentWorkStatusUpdateView,
    CurrentWorkStatusDeleteView,

    ExamCenterCreateView,
    ExamCenterDeleteView,
    ExamCenterUpdateView,

    CoCurricularActivitiesListCreateView,
    CoCurricularActivitiesDeleteView,
    CoCurricularActivitiesUpdateView,

    DGListCreateView,
    DGDeleteView,
    DGUpdateView,
    dg_make_approved,

    AdmissionRulesListCreateView,
    AdmissionRulesDeleteView,
    AdmissionRulesUpdateView,
    admission_rules_approved
)
# from .script import load_applicant
app_name = 'utilities'

urlpatterns = [
    # index url -------------------------------------------------------------
    path('', AcademicIndex.as_view(), name='academic_index'),
    # path('load_applicant/', load_applicant, name='load_applicant'),
    #   Courtesy Title -----------------------------
    path('courtesy-title/list/', CourtesyTitleListCreateView.as_view(),
         name='courtesy-title-list'
         ),
    path('courtesy-title/<int:pk>/delete/', CourtesyTitleDeleteView.as_view(),
         name='courtesy-title-delete'
         ),
    path('courtesy-title/<int:pk>/update/', CourtesyTitleUpdateView.as_view(),
         name='courtesy-title-update'
         ),
    #   Department -------------------------------
    path('department/list/', DepartmentListCreateView.as_view(),
         name='department-list'
         ),
    path('department/<int:pk>/delete/', DepartmentDeleteView.as_view(),
         name='department-delete'
         ),
    path('department/<int:pk>/update/', DepartmentUpdateView.as_view(),
         name='department-update'
         ),
    #   Branch ------------------------------------
    path('branch/list/', BranchListCreateView.as_view(),
         name='branch-list'
         ),
    path('branch/<int:pk>/delete/', BranchDeleteView.as_view(),
         name='branch-delete'
         ),
    path('branch/<int:pk>/update/', BranchUpdateView.as_view(),
         name='branch-update'
         ),
    #   Co-Curricular Activities ------------------------------------
    path('co-curricular/list/',
         CoCurricularActivitiesListCreateView.as_view(),
         name='co-curricular-list'
         ),
    path('co-curricular/<int:pk>/delete/',
         CoCurricularActivitiesDeleteView.as_view(),
         name='co-curricular-delete'
         ),
    path('co-curricular/<int:pk>/update/',
         CoCurricularActivitiesUpdateView.as_view(),
         name='co-curricular-update'
         ),
    #   Teacher Designations -----------------------
    path('teacher-designation/list/',
         TeacherDesignationsListCreateView.as_view(),
         name='teacher-designation-list'
         ),
    path('teacher-designation/<int:pk>/delete/',
         TeacherDesignationsDeleteView.as_view(),
         name='teacher-designation-delete'
         ),
    path('teacher-designation/<int:pk>/update/',
         TeacherDesignationsUpdateView.as_view(),
         name='teacher-designation-update'
         ),
    #   Coach Designations -----------------------
    path('coach-designation/list/',
         CoachDesignationsListCreateView.as_view(),
         name='coach-designation-list'
         ),
    path('coach-designation/<int:pk>/delete/',
         CoachDesignationsDeleteView.as_view(),
         name='coach-designation-delete'
         ),
    path('coach-designation/<int:pk>/update/',
         CoachDesignationsUpdateView.as_view(),
         name='coach-designation-update'
         ),
    #   Employee Designations -----------------------
    path('employee-designation/list/',
         EmployeeDesignationsListCreateView.as_view(),
         name='employee-designation-list'
         ),
    path('employee-designation/<int:pk>/delete/',
         EmployeeDesignationsDeleteView.as_view(),
         name='employee-designation-delete'
         ),
    path('employee-designation/<int:pk>/update/',
         EmployeeDesignationsUpdateView.as_view(),
         name='employee-designation-update'
         ),
    #   Job Type -----------------------
    path('job-type/list/',
         JobTypeListCreateView.as_view(),
         name='job-type-list'
         ),
    path('job-type/<int:pk>/delete/',
         JobTypeDeleteView.as_view(),
         name='job-type-delete'
         ),
    path('job-type/<int:pk>/update/',
         JobTypeUpdateView.as_view(),
         name='job-type-update'
         ),
    #   Current Work-Status -----------------------
    path('work-status/list/',
         CurrentWorkStatusCreateView.as_view(),
         name='work-status-list'
         ),
    path('work-status/<int:pk>/delete/',
         CurrentWorkStatusDeleteView.as_view(),
         name='work-status-delete'
         ),
    path('work-status/<int:pk>/update/',
         CurrentWorkStatusUpdateView.as_view(),
         name='work-status-update'
         ),
    # Exam Center -----------------------
    path('exam-center/list/',
         ExamCenterCreateView.as_view(),
         name='exam-Center-list'
         ),
    path('exam-center/<int:pk>/delete/',
         ExamCenterDeleteView.as_view(),
         name='exam-Center-delete'
         ),
    path('exam-center/<int:pk>/update/',
         ExamCenterUpdateView.as_view(),
         name='exam-Center-update'
         ),

    # Admission Rules -----------------------
    path('dg-sir-profile/list/',
         DGListCreateView.as_view(),
         name='dg_sir_profile_list'
         ),
    path('dg-sir-profile/<int:pk>/delete/',
         DGDeleteView.as_view(),
         name='dg_sir_profile_delete'
         ),
    path('dg-sir-profile/<int:pk>/update/',
         DGUpdateView.as_view(),
         name='dg_sir_profile_update'
         ),
    path('dg-sir-profile/<int:pk>/active/', dg_make_approved,
         name='dg_sir_profile_active'
         ),

    # Admission Rules -----------------------
    path('admission-rules/list/',
         AdmissionRulesListCreateView.as_view(),
         name='admission_rules_list'
         ),
    path('admission-rules/<int:pk>/delete/',
         AdmissionRulesDeleteView.as_view(),
         name='admission_rules_delete'
         ),
    path('admission-rules/<int:pk>/update/',
         AdmissionRulesUpdateView.as_view(),
         name='admission_rules_update'
         ),
    path('admission-rules/<int:pk>/active/', admission_rules_approved,
         name='admission_rules_active'
         ),
]

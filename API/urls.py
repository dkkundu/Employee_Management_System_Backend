"""API > urls.py"""
# DJANGO IMPORTS
from django.urls import path, include
# DRF IMPORTS
from rest_framework.routers import DefaultRouter
# API IMPORTS
from API import views


# /api/... browsable drf api
app_name = 'api'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register('users', views.UserViewSet)

# https://docs.djangoproject.com/en/3.1/topics/http/urls/
urlpatterns = [
    # profile
    path(
        'profiles/<int:pk>/image/',
        views.ImageUploadAPI.as_view(),
        name='profile-image'
    ),

    # auth --------------------------------------------------------------------
    path('auth/signup/', views.UserCreateView.as_view(), name='auth-signup'),
    path('auth/login/', views.ObtainTokenView.as_view(), name='auth-login'),
    path('auth/logout/', views.LogoutView.as_view(), name='auth-logout'),


    path(
        'employee/profile/<int:pk>/', views.EmployeeProfileView.as_view(),
        name='profile'
    ),
    path(
        'employee/list/', views.EmployeeListView.as_view(),
        name='employee_list'
    ),
    path(
        'employee/update/<int:pk>/', views.EmployeeProfileUpdateView.as_view(),
        name='employee_update'
    ),
    path(
        'employee/create/', views.EmployeeCreateView.as_view(),
        name='employee_create'
    ),


    # router ------------------------------------------------------------------
    path('', include(router.urls)),
]

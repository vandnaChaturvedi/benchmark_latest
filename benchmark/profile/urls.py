# Django specific imports
from django.urls import path

# User specific imports
from benchmark.profile import views

urlpatterns = [
    path(
        'submissions/',
        views.UserSubmissionListView.as_view(),
        name='user-submissions'
    ),

    path(
        'update/',
        views.UserUpdateProfile.as_view(),
        name='user-update'
    ),

    path(
        'password_change/',
        views.PasswordChangeCustomView.as_view(),
        name='password-change'
    ),

    path(
        'alerts/',
        views.AlertListView.as_view(),
        name='alerts'
    ),

    path(
        'alerts/delete/',
        views.delete_alerts,
        name='delete-alerts'
    ),
]

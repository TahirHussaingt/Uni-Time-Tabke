"""URL configuration for the University Timetable Management System."""

from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login_preview, name="login-preview"),
    path("student/", views.dashboard, {"page_name": "student"}, name="student-dashboard"),
    path("teacher/", views.dashboard, {"page_name": "teacher"}, name="teacher-dashboard"),
    path("admin-preview/", views.dashboard, {"page_name": "admin"}, name="admin-dashboard"),
]

handler403 = "config.views.error_403"
handler404 = "config.views.error_404"
handler500 = "config.views.error_500"

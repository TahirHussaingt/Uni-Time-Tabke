"""URL configuration for the University Timetable Management System."""

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
]

"""Placeholder views for the reusable Phase 1 visual foundation."""

from django.shortcuts import render


PAGES = {
    "dashboard": {
        "title": "Timetable overview",
        "description": "A visual preview of the official timetable workspace.",
        "context_label": "University workspace",
        "audience": "Overview",
    },
    "student": {
        "title": "Student dashboard",
        "description": "Classes, changes and notices for a student view.",
        "context_label": "Student preview",
        "audience": "Student",
    },
    "teacher": {
        "title": "Teacher dashboard",
        "description": "Teaching schedule and relevant timetable updates.",
        "context_label": "Teacher preview",
        "audience": "Teacher",
    },
    "admin": {
        "title": "Administration dashboard",
        "description": "Schedule status, reviews and operational overview.",
        "context_label": "Administrator preview",
        "audience": "Administrator",
    },
}


def dashboard(request, page_name="dashboard"):
    """Render a clearly labelled, database-free dashboard demonstration."""
    page = PAGES[page_name]
    return render(request, "pages/dashboard.html", {"page": page, "page_name": page_name})


def login_preview(request):
    """Render a visual-only login layout until authentication is implemented."""
    return render(request, "pages/login.html")


def error_403(request, exception=None):
    return render(request, "pages/error.html", {"status_code": "403", "title": "Access restricted"}, status=403)


def error_404(request, exception=None):
    return render(request, "pages/error.html", {"status_code": "404", "title": "Page not found"}, status=404)


def error_500(request):
    return render(request, "pages/error.html", {"status_code": "500", "title": "Something went wrong"}, status=500)

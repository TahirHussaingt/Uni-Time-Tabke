"""Template context shared across the public visual foundation."""

from django.conf import settings


def branding(request):
    """Expose centrally configured institutional branding to templates."""
    return {
        "branding": {
            "university_name": settings.UNIVERSITY_NAME,
            "department_name": settings.UNIVERSITY_DEPARTMENT_NAME,
            "logo_path": settings.UNIVERSITY_LOGO_PATH,
            "logo_available": settings.UNIVERSITY_LOGO_FILE.is_file(),
        }
    }

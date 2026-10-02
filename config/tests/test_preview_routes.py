"""Smoke tests for the Phase 1 visual foundation preview routes."""

from django.conf import settings
from django.test import Client, SimpleTestCase
from django.urls import reverse


class PreviewRouteTests(SimpleTestCase):
    """Verify preview pages respond and expose expected Phase 1 content."""

    def setUp(self):
        self.client = Client()

    def test_home_dashboard(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Timetable overview")
        self.assertContains(response, "Preview mode")
        self.assertContains(response, "Primary navigation")

    def test_dashboard_route(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Timetable overview")

    def test_student_dashboard(self):
        response = self.client.get(reverse("student-dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student dashboard")
        self.assertContains(response, "Student preview")

    def test_teacher_dashboard(self):
        response = self.client.get(reverse("teacher-dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teacher dashboard")
        self.assertContains(response, "Teacher preview")

    def test_admin_preview_dashboard(self):
        response = self.client.get(reverse("admin-dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Administration dashboard")
        self.assertContains(response, "Administrator preview")

    def test_login_preview(self):
        response = self.client.get(reverse("login-preview"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in")
        self.assertContains(response, "Authentication will be implemented in Phase 2")
        self.assertContains(response, settings.UNIVERSITY_NAME)


class BrandingIntegrationTests(SimpleTestCase):
    """Verify centralized branding appears on shell and login preview pages."""

    def setUp(self):
        self.client = Client()

    def test_branding_context_on_dashboard(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, settings.UNIVERSITY_NAME)
        self.assertContains(response, settings.UNIVERSITY_DEPARTMENT_NAME)

    def test_logo_and_favicon_when_asset_present(self):
        if not settings.UNIVERSITY_LOGO_FILE.is_file():
            self.skipTest("Official logo file is not present on disk.")

        home = self.client.get(reverse("home"))
        login = self.client.get(reverse("login-preview"))

        for response in (home, login):
            self.assertContains(response, "FUUAST official logo")
            self.assertContains(response, settings.UNIVERSITY_LOGO_PATH)
            self.assertContains(response, 'rel="icon"')
            self.assertContains(response, "image/svg+xml")

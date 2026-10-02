"""Django application configuration for the project package."""

from django.apps import AppConfig


class ConfigConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "config"
    verbose_name = "Project configuration"

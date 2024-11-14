from django.apps import AppConfig


class TarımConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Tarım"

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()
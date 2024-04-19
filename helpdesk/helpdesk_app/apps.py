from django.apps import AppConfig


class HelpdeskAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'helpdesk_app'

    def ready(self):
        import helpdesk_app.email  # Import the signals module to connect the signals
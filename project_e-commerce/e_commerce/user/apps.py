from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    def ready(self):
        # Import and connect the signal handler function to the user_logged_in signal
        from . import signals


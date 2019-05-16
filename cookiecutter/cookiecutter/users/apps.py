from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "cookiecutter.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import cookiecutter.users.signals  # noqa F401
        except ImportError:
            pass

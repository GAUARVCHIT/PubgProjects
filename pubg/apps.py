from django.apps import AppConfig


class PubgConfig(AppConfig):
    name = 'pubg'

    def ready(self):
        import pubg.signals

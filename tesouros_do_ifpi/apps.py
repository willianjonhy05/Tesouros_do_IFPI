from django.apps import AppConfig


class TesourosDoIfpiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tesouros_do_ifpi'


    def ready(self):
        import tesouros_do_ifpi.signals
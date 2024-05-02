from django.apps import AppConfig

class RestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restapp'

    def ready(self):   
        from . import updater 	
        updater.start()

from django.apps import AppConfig


class DocConfig(AppConfig):
    name = "cotidia.doc"
    label = "doc"

    def ready(self):
        import cotidia.doc.signals

from django.apps import AppConfig


class DocPatientConfig(AppConfig):
    name = 'doc_patient'
    def ready(self):
        import doc_patient.signals 
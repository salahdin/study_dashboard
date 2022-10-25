from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'study_dashboard'
    admin_site_name = 'study_subject_admin'




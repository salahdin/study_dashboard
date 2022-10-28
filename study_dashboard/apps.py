from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'study_dashboard'
    admin_site_name = 'study_subject_admin'


if settings.APP_NAME == "subject_dashboard":
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        configurations = [
            AppointmentConfig(
                model='study_subject.appointment',
                related_visit_model='cancer_dashboard.subjectvisit',
                appt_type='hospital')]

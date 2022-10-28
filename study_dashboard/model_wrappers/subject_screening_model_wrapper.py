from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_model_wrapper import ModelWrapper
from django.conf import settings


class SubjectScreeningModelWrappers(ModelWrapper):
    model = 'study_subject.subjectscreening'
    next_url_attrs = ['subject_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'subject_dashboard_url')

    @property
    def subject_screening_model_obj(self):
        try:
            return self.subject_screening_cls.objects.get(**self.subject_screening_options)
        except ObjectDoesNotExist:
            return None

    @property
    def subject_screening_cls(self):
        return django_apps.get_model('study_subject.subjectscreening')

    @property
    def subject_screening_options(self):
        options = dict(
            subject_identifier=self.subject_identifier
        )
        return options

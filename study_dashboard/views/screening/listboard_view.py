import re

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import ABNORMAL
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from ...model_wrappers import SubjectScreeningModelWrappers


class ListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                    ListboardFilterViewMixin, SearchFormViewMixin,
                    ListboardView):
    listboard_template = 'screening_listboard_template'
    listboard_url = 'screening_listboard_url'

    model_wrapper_cls = SubjectScreeningModelWrappers

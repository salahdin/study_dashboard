from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'cancer_dashboard' else False

study_dashboard = Navbar(name='cancer_dashboard')

study_dashboard.append_item(
    NavbarItem(
        name='consented_subject',
        title='Subjects',
        label='subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES['subject_listboard_url'],
        no_url_namespace=no_url_namespace))

site_navbars.register(study_dashboard)

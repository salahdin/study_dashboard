from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'study_dashboard' else False

study_dashboard = Navbar(name='study_dashboard')


study_dashboard.append_item(
    NavbarItem(
        name='eligible_subject',
        title='Subject Screening',
        label='Subject Screening',
        fa_icon='fa fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES[
            'screening_listboard_url'],
        no_url_namespace=no_url_namespace))

site_navbars.register(study_dashboard)



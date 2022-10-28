from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Study Subject'
    site_header = 'Study Subject'
    index_title = 'Study Subject'
    site_url = '/administration/'

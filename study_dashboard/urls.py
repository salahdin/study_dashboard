from django.conf import settings
from django.conf import settings
from django.urls.conf import path, include
from edc_appointment.admin_site import edc_appointment_admin
from edc_dashboard import UrlConfig

urlpatterns = []

if settings.APP_NAME == 'study_dashboard':

    from django.views.generic.base import RedirectView
    from edc_base.auth.views import LoginView, LogoutView

    #from .tests.admin import subject_test_admin

    urlpatterns += [
        path('edc_device/', include('edc_device.urls')),
        path('edc_protocol/', include('edc_protocol.urls')),
        path('admin/', edc_appointment_admin.urls),

        path('admininistration/', RedirectView.as_view(url='admin/'),
             name='administration_url'),
        path('accounts/', include('edc_base.auth.urls')),
        path('admin/', include('edc_base.auth.urls')),
        path('edc_lab/', include('edc_lab.urls')),
        path('edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
        path('login', LoginView.as_view(), name='login_url'),
        path('logout', LogoutView.as_view(), name='logout_url'),
        path(r'', RedirectView.as_view(url='admin/'), name='home_url')]
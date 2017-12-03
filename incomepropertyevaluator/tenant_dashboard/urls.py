from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from tenant_dashboard import views


urlpatterns = (
    url(r'^dashboard$', views.master_page, name='mika_tenant_dashboard_master'),
)

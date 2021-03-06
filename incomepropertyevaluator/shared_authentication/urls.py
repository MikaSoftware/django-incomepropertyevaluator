from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from shared_authentication.views import email_views
from shared_authentication.views import web_views


urlpatterns = (
    # EMAIL
    url(r'^activate/(.*)/email/$',
    email_views.user_activation_email_page,
    name='at_user_activation_email_master'),

    # WEB
    url(r'^sign-in$',
    web_views.user_login_master_page,
    name='at_login_master'),

    url(r'^sign-in-redirect$',
    web_views.user_login_redirect,
    name='mika_login_redirect'),

    url(r'^register/$',
    web_views.register_master_page,
    name='at_register_master'),

    url(r'^register/done$',
    web_views.register_detail_page,
    name='at_register_detail'),

    url(r'^activate/(.*)/$',
    web_views.user_activation_detail_page,
    name='at_user_activation_detail'),
)

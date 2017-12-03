from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import serializers, viewsets, routers
from rest_framework.urlpatterns import format_suffix_patterns
from shared_authentication.views.api_login_view import LoginAPIView
from shared_authentication.views.api_logout_view import LogoutAPIView
from shared_authentication.views.api_obtainauthtoken_view import ObtainAuthTokenAPIView # DEPRECATED
from shared_authentication.views.api_register_user_view import RegisterUserAPIView
from shared_authentication.views.api_register_organization_view import RegisterOrganizationAPIView


urlpatterns = [
    # Authentication.
    url(r'^api/login$', LoginAPIView.as_view()),
    url(r'^api/logout$', LogoutAPIView.as_view()),
    url(r'^api/get_token$', ObtainAuthTokenAPIView.as_view()), # DEPRECATED
    url(r'^api/register/user/$', RegisterUserAPIView.as_view()),
    #
    # Organization
    url(r'^api/register/organization/$', RegisterOrganizationAPIView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import serializers, viewsets, routers
from rest_framework.urlpatterns import format_suffix_patterns
from shared_authentication.views.api_login_view import LoginAPIView
from shared_authentication.views.api_logout_view import LogoutAPIView
from shared_authentication.views.api_register_view import RegisterAPIView


urlpatterns = [
    # Authentication.
    url(r'^api/login$', LoginAPIView.as_view()),
    url(r'^api/logout$', LogoutAPIView.as_view()),
    url(r'^api/register$', RegisterAPIView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
